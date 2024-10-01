#STEP 0: IMPORTS #test187
from typing import Final 
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message, Game 
from responses import get_responses
import random
from database import log_message, show_messages

#STEP 1: LOAD TOKEN FROM SOMWHERE SAFE
load_dotenv()

"""
 Diese Funktion lädt die Umgebungsvariablen aus einer .env-Datei im Projekt-Stammverzeichnis 
    und ruft den Wert der Variable "DISCORD_TOKEN" ab.

    Funktionalität:
    1. `load_dotenv()` ist eine Funktion aus dem Python-Modul dotenv. Sie liest das Schlüssel-Wert-Paar aus der .env-Datei 
       und fügt sie den Umgebungsvariablen hinzu. Sie wird hier verwendet, um das DISCORD_TOKEN aus der .env-Datei zu laden.
    2. `os.getenv("DISCORD_TOKEN")` wird verwendet, um den Wert der Umgebungsvariable 'DISCORD_TOKEN' abzurufen. 
       Wenn die Umgebungsvariable nicht gefunden wird, gibt sie None zurück.

    Eingabe: Keine

    Ausgabe: 
    - TOKEN: Final[str] - Der Wert der Umgebungsvariable "DISCORD_TOKEN" als Zeichenkette. 
      Wenn die Variable nicht gefunden wird, ist der Wert None.
"""

TOKEN: Final[str] = os.getenv("DISCORD_TOKEN")      #Final is a type hint that tells the reader that the variable is a constant and immutable
#print(TOKEN)                                       <-Check if token is loaded correctly

#STEP 2: BOT SETUP
intents: Intents = Intents.default()                #Make the bot be able to read messages 
intents.message_content = True 
client: Client = Client(intents=intents)

#STEP 3: MESSAGE FUNCTIONALITY 
async def send_message(message: Message, user_message: str) -> None:        #asynchronous function, which means that the function can run in the background while the rest of the code runs

    """
    Asynchrone Funktion zum Senden einer Nachricht an einen Benutzer oder einen Kanal.

    Diese Funktion nimmt ein Message-Objekt und einen Benutzernachricht-String als Eingabe. Wenn der Benutzernachricht-String nicht leer ist, 
    überprüft sie, ob die Nachricht privat gesendet werden soll (wenn das erste Zeichen "!"). Wenn ja, wird das "!" entfernt 
    und die Antwort privat an den Autor der Nachricht gesendet. Wenn nicht, wird die Antwort an den Kanal gesendet. 
    Wenn während des Prozesses eine Ausnahme auftritt, wird diese Ausnahme ausgegeben.

    Args:
        message (Message): Das Message-Objekt, das Informationen über den Autor und den Kanal enthält.
        user_message (str): Die Nachricht vom Benutzer. Wenn das erste Zeichen "!", soll die Nachricht privat gesendet werden.

    Returns:
        None
    """

    if not user_message:
        print("Fehler")
        return
    
    if is_private := user_message[0] == "!":        #Check if the message is meant to be sent privately (if the first character is "!" then the message is meant to be sent privately)
        user_message = user_message[1:]
    
    try:
        response: str = get_responses(user_message)     
        await message.author.send(response) if is_private else await message.channel.send(response)   #Send the response privately if the message is meant to be sent privately
    except Exception as e:
        print(e) 
    
#STEP 4: EVENT HANDLER: STARTUP
@client.event
async def on_ready() -> None:

    """"
    Asynchrone Funktion, die ausgeführt wird, wenn der Bot bereit ist.

    Diese Funktion gibt eine Nachricht aus, dass der Bot jetzt dabei ist und ändert dann den Status des Bots, 
    um anzuzeigen, auf wie vielen Servern er gerade spielt.

    Args:
        Keine

    Returns:
        None
    """

    print(f'{client.user} ist jetzt dabei!')
    await client.change_presence(activity=Game(name=f"Auf {len(client.guilds)} Servern mit"))           #Change the status of the bot (playing on x servers)

#STEP 5: EVENT HANDLER: MESSAGE
@client.event
async def on_message(message: Message) -> None:

    """
    Asynchrone Funktion, die ausgeführt wird, wenn eine Nachricht empfangen wird.

    Diese Funktion überprüft zunächst, ob die Nachricht vom Bot selbst stammt. Wenn ja, wird die Funktion beendet. 
    Wenn nicht, werden der Benutzername, die Benutzernachricht und der Kanal aus der Nachricht extrahiert. 
    Die Nachricht wird dann in der Datenbank protokolliert und in der Konsole ausgegeben. 
    Schließlich wird die Funktion `send_message` aufgerufen, um eine Antwort zu senden.

    Args:
        message (Message): Die empfangene Nachricht.

    Returns:
        None
    """
    
    if message.author == client.user:
        return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    log_message(username, user_message, channel)                                                             #Log the message in the database

    print(f"User: {username} | Message: {user_message} | Channel: {channel}")                           #Log the message, user and channel in the console
    await send_message(message, user_message)

#STEP 6: RUN THE BOT
def main() -> None:                                                                                #Function to run the bot
    
    """
    Funktion zum Starten des Bots.

    Diese Funktion startet den Bot durch Aufrufen der `run`-Methode des `client`-Objekts mit dem Token als Argument.

    Args:
        Keine

    Returns:
        None
    """
    
    client.run(token=TOKEN)             

if __name__ == "__main__":                  
    try:                                                                                  
        main()  
    finally:
        show_messages()                                                                                          #Show all messages in the database

#11111111111111111111111111111111111111111111111111111111111111#11111111111111111111111111111111111111111111111111111111111111111111111111111
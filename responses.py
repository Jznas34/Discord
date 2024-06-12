from random import choice, randint 
from weatherapi import get_weather
from meddler import drache_zitat

def get_responses(user_input : str) -> str:         #Function that returns a response based on the user input
    command = user_input.split()[0].lower()

# Itereate over the messages and return the appropriate response

    if command == "/hallo":
        return "Hallo! Wie kann ich dir helfen?"
    
    elif "/würfeln" in command:
        return f"Du hast eine {randint(1, 6)} gewürfelt!"
    
    elif "/help" in command:
        return "Hier ist eine Liste aller Befehle:\n /help \n /meddl \n /wetter 'Stadt' \n /würfeln \n Schreibe ! vor deinen Command, um die Antwort als DM zu erhalten, z.B. '!/help'."
    
    elif "/wetter" in command:
        location = ' '.join(user_input.split()[1:])
        return get_weather(location)

    elif "/meddl" in command:
        return drache_zitat()

    else:
        return choice([
            "Diesen Befehl kenne ich nicht. Mit /help bekommst du eine Liste aller Befehle",
        ])
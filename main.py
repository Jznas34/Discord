#Hallo test test
#git add 
#git commit -m "msg"
#git 


#STEP 0: IMPORTS
from typing import Final 
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_responses

#STEP 1: LOAD TOKEN FROM SOMWHERE SAFE
load_dotenv()
TOKEN: Final[str] = os.getenv("DISCORD_TOKEN")      #Final is a type hint that tells the reader that the variable is a constant and immutable
#print(TOKEN)                                       <-Check if token is loaded correctly

#STEP 2: BOT SETUP
intents: Intents = Intents.default()                #Make the bot be able to read messages 
intents.message_content = True 
client: Client = Client(intents=intents)

#STEP 3: MESSAGE FUNCTIONALITY 
async def send_message(message: Message, user_message: str) -> None:    
    if not user_message:
        print("Fehler")
        return
    
    if is_private := user_message[0] == "?":        #Check if the message is meant to be sent privately (if the first character is a question mark)
        user_message = user_message[1:]
    
    try:
        response: str = get_responses(user_message)     
        await message.author.send(response) if is_private else message.channel.send(response)   #Send the response privately if the message is meant to be sent privately
    except Exception as e:
        print(e) 

#STEP 4: EVENT HANDLERS: STARTUP
@client.event
async def on_ready() -> None:
    print(f'{client.user} has connected to Discord!')

#STEP 5: EVENT HANDLERS: MESSAGE
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f"User: {username} | Message: {user_message} | Channel: {channel}")
    await send_message(message, user_message)

    
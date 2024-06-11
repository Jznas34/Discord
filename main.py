#Hallo test test
#git add 
#git commit -m "msg"
#git 

from typing import Final 
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_responses

#LOAD TOKEN FROM SOMWHERE SAFE

load_dotenv()
TOKEN: Final[str] = os.getenv("DISCORD_TOKEN")
print(TOKEN)
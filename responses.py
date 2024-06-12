from random import choice, randint 
from weatherapi import get_weather

def get_responses(user_input : str) -> str:
    command = user_input.split()[0].lower()

    if command == "/hallo":
        return "Hallo! Wie kann ich dir helfen?"
    
    elif "/würfeln" in command:
        return f"Du hast eine {randint(1, 6)} gewürfelt!"
    
    elif "/help" in command:
        return "Hier ist eine Liste aller Befehle:\n /help \n /meddl \n /wetter *Stadt* \n /würfeln \n ! für DM -> !/help."
    
    elif "/wetter" in command:
        location = ' '.join(user_input.split()[1:])
        return get_weather(location)

    else:
        return choice([
            "Diesen Befehl kenne ich nicht. Mit /help bekommst du eine Liste aller Befehle",
        ])
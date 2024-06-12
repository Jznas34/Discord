from random import choice, randint 

def get_responses(user_input : str) -> str:
    input: str = user_input.lower()   

    if input == "/hallo":
        return "Hallo! Wie kann ich dir helfen?"
    
    elif "/würfeln" in input:
        return f"Du hast eine {randint(1, 6)} gewürfelt!"
    
    elif "/help" in input:
        return "Wenn du direkt vor deine Nachricht ! schreibst, wird dir die Antwort per DM geschickt. Hier eine Liste aller Befehle: \n /hallo \n /würfeln"

    

    else:
        return choice([
            "Diesen Befehl kenne ich nicht. Mit /help bekommst du eine Liste aller Befehle",
        ])
import random

def drache_zitat() -> str:                                           #function that returns a random quote from a file
    with open("meddl.txt", "r", encoding="UTF-8") as data:
        quotes = data.readlines()
        return random.choice(quotes).strip()
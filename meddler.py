import random

def drache_zitat() -> str:                                           #function that returns a random quote from a file

    """
    Diese Funktion liest eine Datei mit Zitaten ein und gibt ein zufälliges Zitat zurück.

    Returns:
    str: Ein zufällig ausgewähltes Zitat aus der Datei "meddl.txt". Das Zitat wird als String zurückgegeben.

    Die Funktion öffnet die Datei "meddl.txt" im Lese-Modus und liest alle Zeilen in eine Liste ein. 
    Anschließend wird ein Zitat zufällig aus dieser Liste ausgewählt und zurückgegeben. 
    Vor der Rückgabe wird die strip()-Methode auf das Zitat angewendet, um überflüssige Leerzeichen am Anfang und Ende des Zitats zu entfernen.
    """

    with open("meddl.txt", "r", encoding="UTF-8") as data:
        quotes = data.readlines()
        return random.choice(quotes).strip()
import sqlite3

# Connect to sqlite database
conn = sqlite3.connect('chatlog.db')

# Create a cursor
c = conn.cursor()

# Create table
c.execute('''
    CREATE TABLE IF NOT EXISTS chatlog (
        id INTEGER PRIMARY KEY,
        username TEXT,
        message TEXT,
        channel TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
''')

# Commit changes and close connection
conn.commit()
conn.close()


def log_message(username, message, channel):                        #Function to log messages in the database

    """
    Funktion zum Protokollieren von Nachrichten in der Datenbank.

    Diese Funktion nimmt einen Benutzernamen, eine Nachricht und einen Kanal als Eingabe und fügt diese Informationen 
    in die Tabelle `chatlog` der Datenbank `chatlog.db` ein. Nach dem Einfügen der Daten wird die Datenbankverbindung 
    geschlossen.

    Args:
        username (str): Der Benutzername des Autors der Nachricht.
        message (str): Die Nachricht, die protokolliert werden soll.
        channel (str): Der Kanal, in dem die Nachricht gesendet wurde.

    Returns:
        None
    
    """

    conn = sqlite3.connect('chatlog.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO chatlog (username, message, channel)
        VALUES (?, ?, ?)
    ''', (username, message, channel))
    conn.commit()
    conn.close()

def show_messages():                                                #Function to show all messages in the database

    """
    Funktion zum Anzeigen aller Nachrichten in der Datenbank.

    Diese Funktion stellt eine Verbindung zur Datenbank `chatlog.db` her, führt eine SQL-Abfrage aus, um alle Einträge 
    aus der Tabelle `chatlog` zu holen, und druckt dann jede Zeile in einem formatierten String aus, der die Zeitstempel, 
    den Benutzernamen, den Kanal und die Nachricht enthält. Nach dem Ausgeben aller Zeilen wird die Datenbankverbindung 
    geschlossen.

    Args:
        Keine

    Returns:
        None
    """

    conn = sqlite3.connect('chatlog.db')
    c = conn.cursor()
    c.execute('SELECT * FROM chatlog')
    for row in c.fetchall():
        id, username, message, channel, timestamp = row
        print(f"{timestamp} - {username} in {channel}: {message}")
    conn.close()
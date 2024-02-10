import sqlite3

def init_db():
    # Creates new database
    conn = sqlite3.connect('dpl_database.db')
    cursor = conn.cursor()

    # Create the Players table if it doesn't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Players (
        PlayerID INTEGER PRIMARY KEY AUTOINCREMENT,
        FirstName TEXT,
        LastName TEXT
    )
    ''')
    # Create the Matches table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Matches (
            MatchID INTEGER PRIMARY KEY AUTOINCREMENT,
            MatchDate DATE,
            Location TEXT, 
            GameType TEXT
        )
    ''')
    # Create the MatchStats table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS MatchStats (
            StatID INTEGER PRIMARY KEY AUTOINCREMENT,
            PlayerID INTEGER,
            MatchID INTEGER,
            AverageTurnScore REAL,
            NumberOf180s INTEGER,
            MatchWinnerPlayerID INTEGER,
            FOREIGN KEY (PlayerID) REFERENCES Players(PlayerID),
            FOREIGN KEY (MatchID) REFERENCES Matches(MatchID)
        )
    ''')
    # Create the DartThrows table if it doesn't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS DartThrows (
        ThrowID INTEGER PRIMARY KEY AUTOINCREMENT,
        PlayerID INTEGER,  
        Score INTEGER, 
        Multiplier INTEGER, 
        Value INTEGER,
        IsBounceOut BOOLEAN,
        IsKnockOut BOOLEAN,
        IsFoulOut BOOLEAN,
        FOREIGN KEY (PlayerID) REFERENCES Players(PlayerID) 
    )
    ''')


    # Create the Combinations table if it doesn't exist
    cursor.execute('''
         CREATE TABLE IF NOT EXISTS Combinations (
             Score INTEGER,
             Combinations TEXT
         )
     ''')

    # Commit and close the database connection
    conn.commit()
    conn.close()


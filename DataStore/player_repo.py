import sqlite3

database_name = 'dpl_database.db'

def connect_db():
    return sqlite3.connect(database_name)

def close_db(conn):
    if conn:
        conn.close()

def table_exists(table_name):
    conn = connect_db()
    cursor = conn.cursor()

    try:
        cursor.execute(f'SELECT 1 FROM {table_name} LIMIT 1;')
        return True
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return False
    finally:
        close_db(conn)

def add_player(first_name, last_name):
    with connect_db() as conn:
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM Players WHERE FirstName = ? AND LastName = ?', (first_name, last_name))
        player = cursor.fetchone()

        if player:
            return

        cursor.execute('''
        INSERT INTO Players (FirstName, LastName)
        VALUES (?, ?)
        ''', (first_name, last_name))

        conn.commit()

def update_player(player_id, first_name=None, last_name=None):
    conn = connect_db()
    cursor = conn.cursor()

    # Check if player exists in the table
    cursor.execute('SELECT COUNT(*) FROM Players WHERE PlayerID = ?', (player_id,))
    if cursor.fetchone()[0] == 0:
        print(f"Player with PlayerID {player_id} does not exist in the table.")
        close_db(conn)
        return

    # Dynamically build the update statement based on provided values
    columns_to_update = []
    values_to_update = []

    if first_name is not None:
        columns_to_update.append("FirstName = ?")
        values_to_update.append(first_name)

    if last_name is not None:
        columns_to_update.append("LastName = ?")
        values_to_update.append(last_name)

    if not columns_to_update:
        print("No updates provided.")
        close_db(conn)
        return

    update_stmt = "UPDATE Players SET " + ", ".join(columns_to_update) + " WHERE PlayerID = ?"
    values_to_update.append(player_id)
    cursor.execute(update_stmt, tuple(values_to_update))

    conn.commit()
    close_db(conn)



def delete_player_by_id(player_id):
    conn = connect_db()
    cursor = conn.cursor()

    # Check if the player exists in the table
    cursor.execute('SELECT COUNT(*) FROM Players WHERE PlayerID = ?', (player_id,))
    if cursor.fetchone()[0] == 0:
        print(f"Player with PlayerID {player_id} does not exist in the table.")
        close_db(conn)
        return

    # Delete the player by their Player ID
    cursor.execute('DELETE FROM Players WHERE PlayerID = ?', (player_id,))

    conn.commit()
    close_db(conn)

def get_player_id_by_name(first_name, last_name):
    conn = connect_db()
    cursor = conn.cursor()

    try:
        # Query to find the player by first and last name
        cursor.execute('SELECT PlayerID FROM Players WHERE FirstName = ? AND LastName = ?', (first_name, last_name))
        result = cursor.fetchone()
        return result[0] if result else None
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return None
    finally:
        close_db(conn)


def print_all_players():
    conn = connect_db()
    cursor = conn.cursor()

    try:
        cursor.execute('SELECT PlayerID, FirstName, LastName FROM Players')
        players = cursor.fetchall()

        if players:
            for player in players:
                print(f"Player ID: {player[0]}, Name: {player[1]} {player[2]}")
        else:
            print("No players found in the database.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        close_db(conn)


def get_list():
    conn = connect_db()
    cursor = conn.cursor()

    try:
        cursor.execute('SELECT FirstName, LastName FROM Players')
        players = cursor.fetchall()

        player_list = [{'first_name': player[0], 'last_name': player[1]} for player in players]
        return player_list

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return []
    finally:
        close_db(conn)
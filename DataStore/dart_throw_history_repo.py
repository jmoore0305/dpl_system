import sqlite3

database_name = 'dpl_database.db'

def connect_db():
    return sqlite3.connect(database_name)

def close_db(conn):
    if conn:
        conn.close()

def get_second_last_throw_id():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT ThrowID
        FROM DartThrows
        ORDER BY ThrowID DESC
        LIMIT 1 OFFSET 1
    ''')

    result = cursor.fetchone()
    close_db(conn)
    return result[0] if result else None



def get_last_throw_id():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT ThrowID
        FROM DartThrows
        ORDER BY ThrowID DESC
        LIMIT 1
    ''')

    result = cursor.fetchone()
    close_db(conn)
    return result[0] if result else None



def add_throw(player_id, score, multiplier, value, is_bounce_out, is_knock_out, is_foul_out):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO DartThrows (PlayerID, Score, Multiplier, Value, IsBounceOut, IsKnockOut, IsFoulOut)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (player_id, score, multiplier, value, is_bounce_out, is_knock_out, is_foul_out))

    conn.commit()
    close_db(conn)

def update_throw(player_id, score=None, multiplier=None, value=None, is_bounce_out=None, is_knock_out=None, is_foul_out=None):
    conn = connect_db()
    cursor = conn.cursor()

    columns_to_update = []
    values_to_update = []

    if score is not None:
        columns_to_update.append("Score = ?")
        values_to_update.append(score)

    if multiplier is not None:
        columns_to_update.append("Multiplier = ?")
        values_to_update.append(multiplier)

    if value is not None:
        columns_to_update.append("Value = ?")
        values_to_update.append(value)

    if is_bounce_out is not None:
        columns_to_update.append("IsBounceOut = ?")
        values_to_update.append(is_bounce_out)

    if is_knock_out is not None:
        columns_to_update.append("IsKnockOut = ?")
        values_to_update.append(is_knock_out)

    if is_foul_out is not None:
        columns_to_update.append("IsFoulOut = ?")
        values_to_update.append(is_foul_out)

    values_to_update.append(player_id)

    update_stmt = "UPDATE DartThrows SET " + ", ".join(columns_to_update) + " WHERE PlayerID = ?"
    cursor.execute(update_stmt, values_to_update)

    conn.commit()
    close_db(conn)


def update_throw_by_throw_id(throw_id, score=None, multiplier=None, value=None, is_bounce_out=None, is_knock_out=None, is_foul_out=None):
    conn = connect_db()
    cursor = conn.cursor()

    columns_to_update = []
    values_to_update = []

    if score is not None:
        columns_to_update.append("Score = ?")
        values_to_update.append(score)

    if multiplier is not None:
        columns_to_update.append("Multiplier = ?")
        values_to_update.append(multiplier)

    if value is not None:
        columns_to_update.append("Value = ?")
        values_to_update.append(value)

    if is_bounce_out is not None:
        columns_to_update.append("IsBounceOut = ?")
        values_to_update.append(is_bounce_out)

    if is_knock_out is not None:
        columns_to_update.append("IsKnockOut = ?")
        values_to_update.append(is_knock_out)

    if is_foul_out is not None:
        columns_to_update.append("IsFoulOut = ?")
        values_to_update.append(is_foul_out)

    values_to_update.append(throw_id)

    update_stmt = "UPDATE DartThrows SET " + ", ".join(columns_to_update) + " WHERE ThrowID = ?"
    cursor.execute(update_stmt, values_to_update)

    conn.commit()
    close_db(conn)




def get_all_throws_for_player(player_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT Score, IsBounceOut, IsKnockOut, IsFoulOut 
        FROM DartThrows 
        WHERE PlayerID = ?
    ''', (player_id,))

    throws = cursor.fetchall()

    close_db(conn)
    return throws

def get_last_ten_throws_for_player(player_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT Score, IsBounceOut, IsKnockOut, IsFoulOut 
        FROM DartThrows 
        WHERE PlayerID = ?
        ORDER BY ThrowID DESC
        LIMIT 10
    ''', (player_id,))

    # Fetch the last ten throws
    throws = cursor.fetchall()

    close_db(conn)
    return throws

def get_last_ten_throws_for_all():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT Score, IsBounceOut, IsKnockOut, IsFoulOut 
        FROM DartThrows 
        ORDER BY ThrowID DESC
        LIMIT 10
    ''',)

    # Fetch the last ten throws
    throws = cursor.fetchall()

    close_db(conn)
    return throws

def delete_all_throws():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('DELETE FROM DartThrows')

    conn.commit()
    close_db(conn)

def get_last_entry_player_id():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT PlayerID 
        FROM DartThrows 
        ORDER BY ThrowID DESC 
        LIMIT 1
    ''')

    result = cursor.fetchone()
    close_db(conn)
    return result[0] if result else None

def delete_last_throw():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM DartThrows 
        WHERE ThrowID = (SELECT MAX(ThrowID) FROM DartThrows)
    ''')
    conn.commit()
    close_db(conn)
    print("Last throw deleted successfully.")

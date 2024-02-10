import sqlite3

database_name = 'dpl_database.db'

def connect_db():
    return sqlite3.connect(database_name)

def close_db(conn):
    if conn:
        conn.close()

def add_match_stats(player_id, match_id, average_turn_score=None, number_of_180s=None, match_winner_player_id=None):
    conn = connect_db()
    cursor = conn.cursor()

    # Round the average_turn_score to 2 decimal places
    rounded_average_turn_score = round(average_turn_score, 2) if average_turn_score is not None else None

    cursor.execute('''
    INSERT INTO MatchStats (PlayerID, MatchID, AverageTurnScore, NumberOf180s, MatchWinnerPlayerID)
    VALUES (?, ?, ?, ?, ?)
    ''', (player_id, match_id, rounded_average_turn_score, number_of_180s, match_winner_player_id))

    conn.commit()
    close_db(conn)

def print_all_match_stats():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM MatchStats')
    stats = cursor.fetchall()

    if stats:
        for stat in stats:
            print(f"StatID: {stat[0]}, PlayerID: {stat[1]}, MatchID: {stat[2]}, " +
                  f"AverageTurnScore: {stat[3]}, NumberOf180s: {stat[4]}, MatchWinnerPlayerID: {stat[5]}")
    else:
        print("No match stats found.")

    close_db(conn)

def get_match_stats_by_id(stat_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM MatchStats WHERE StatID = ?', (stat_id,))
    stat = cursor.fetchone()

    close_db(conn)
    return stat

def update_match_stats(player_id, match_id, average_turn_score=None, number_of_180s=None, match_winner_player_id=None):
    conn = connect_db()
    cursor = conn.cursor()

    if isinstance(average_turn_score, list):
        if len(average_turn_score) > 0:
            average_turn_score = sum(average_turn_score) / len(average_turn_score)
        else:
            average_turn_score = None

    rounded_average_turn_score = round(average_turn_score, 2) if average_turn_score is not None else None

    cursor.execute('''
    UPDATE MatchStats
    SET AverageTurnScore = ?, NumberOf180s = ?, MatchWinnerPlayerID = ?
    WHERE PlayerID = ? AND MatchID = ?
    ''', (rounded_average_turn_score, number_of_180s, match_winner_player_id, player_id, match_id))

    conn.commit()
    close_db(conn)


def delete_match_stats_by_id(stat_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('DELETE FROM MatchStats WHERE StatID = ?', (stat_id,))

    conn.commit()
    close_db(conn)

def get_last_stats_id():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('SELECT MAX(StatID) FROM MatchStats')
    stat_id = cursor.fetchone()

    close_db(conn)

    return stat_id[0] if stat_id else None



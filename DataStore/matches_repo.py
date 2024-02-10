import sqlite3
import datetime

database_name = 'dpl_database.db'

def connect_db():
    return sqlite3.connect(database_name)

def close_db(conn):
    if conn:
        conn.close()
def get_match_date_by_id(match_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('SELECT MatchDate FROM Matches WHERE MatchID = ?', (match_id,))
    match_date = cursor.fetchone()

    close_db(conn)

    return match_date[0] if match_date else None

def add_match(match_date, location, game_type):
    with connect_db() as conn:
        cursor = conn.cursor()

        cursor.execute('''
        INSERT INTO Matches (MatchDate, Location, GameType)
        VALUES (?, ?, ?)
        ''', (match_date, location, game_type))

        conn.commit()

def update_match(match_id, match_date=None, location=None, game_type=None):
    conn = connect_db()
    cursor = conn.cursor()

    columns_to_update = []
    values_to_update = []

    if match_date is not None:
        columns_to_update.append("MatchDate = ?")
        values_to_update.append(match_date)

    if location is not None:
        columns_to_update.append("Location = ?")
        values_to_update.append(location)

    if game_type is not None:
        columns_to_update.append("GameType = ?")
        values_to_update.append(game_type)

    if not columns_to_update:
        print("No updates provided.")
        close_db(conn)
        return

    update_stmt = "UPDATE Matches SET " + ", ".join(columns_to_update) + " WHERE MatchID = ?"
    values_to_update.append(match_id)
    cursor.execute(update_stmt, tuple(values_to_update))

    conn.commit()
    close_db(conn)

def delete_match_by_id(match_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('SELECT COUNT(*) FROM Matches WHERE MatchID = ?', (match_id,))
    if cursor.fetchone()[0] == 0:
        print(f"Match with MatchID {match_id} does not exist in the table.")
        close_db(conn)
        return

    cursor.execute('DELETE FROM Matches WHERE MatchID = ?', (match_id,))
    conn.commit()
    close_db(conn)

def print_all_matches():
    conn = connect_db()
    cursor = conn.cursor()

    try:
        cursor.execute('SELECT MatchID, MatchDate, Location, GameType FROM Matches')
        matches = cursor.fetchall()

        if matches:
            for match in matches:
                print(f"Match ID: {match[0]}, Date: {match[1]}, Location: {match[2]}, Type: {match[3]}")
        else:
            print("No matches found in the database.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        close_db(conn)

def get_last_match_id():
    conn = connect_db()
    cursor = conn.cursor()

    try:
        cursor.execute('SELECT MatchID FROM Matches ORDER BY MatchID DESC LIMIT 1')
        result = cursor.fetchone()
        return result[0] if result else None
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return None
    finally:
        close_db(conn)


def get_season(date):
    year = date.year
    spring = (datetime.date(year, 3, 21), datetime.date(year, 6, 20))
    summer = (datetime.date(year, 6, 21), datetime.date(year, 9, 22))
    fall = (datetime.date(year, 9, 23), datetime.date(year, 12, 20))
    winter_start = datetime.date(year, 12, 21)
    winter_end = datetime.date(year + 1, 3, 20)

    if spring[0] <= date <= spring[1]:
        return spring
    elif summer[0] <= date <= summer[1]:
        return summer
    elif fall[0] <= date <= fall[1]:
        return fall
    else:
        return (winter_start, winter_end)



def get_total_180s_in_season(player_id):
    conn = connect_db()
    cursor = conn.cursor()

    last_match_id = get_last_match_id()

    current_match_date = get_match_date_by_id(last_match_id)

    current_match_date = datetime.datetime.strptime(current_match_date, "%m/%d/%Y").date()

    season_start, season_end = get_season(current_match_date)

    season_start_str = season_start.strftime("%m/%d/%Y")
    season_end_str = season_end.strftime("%m/%d/%Y")

    cursor.execute('''
        SELECT SUM(MatchStats.NumberOf180s) 
        FROM MatchStats 
        JOIN Matches ON MatchStats.MatchID = Matches.MatchID
        WHERE Matches.MatchDate BETWEEN ? AND ? AND MatchStats.PlayerID = ?
    ''', (season_start_str, season_end_str, player_id))

    total_180s = cursor.fetchone()[0]

    close_db(conn)

    return str(total_180s) if total_180s is not None else "0"







def get_average_turn_score_in_season(player_id):
    conn = connect_db()
    cursor = conn.cursor()

    last_match_id = get_last_match_id()
    current_match_date = get_match_date_by_id(last_match_id)
    current_match_date = datetime.datetime.strptime(current_match_date, "%m/%d/%Y").date()
    season_start, season_end = get_season(current_match_date)

    season_start_str = season_start.strftime("%m/%d/%Y")
    season_end_str = season_end.strftime("%m/%d/%Y")

    cursor.execute('''
        SELECT SUM(MatchStats.AverageTurnScore), COUNT(MatchStats.StatID) 
        FROM MatchStats 
        JOIN Matches ON MatchStats.MatchID = Matches.MatchID
        WHERE Matches.MatchDate BETWEEN ? AND ? AND MatchStats.PlayerID = ?
    ''', (season_start_str, season_end_str, player_id))

    sum_turn_score, count_turn_score = cursor.fetchone()

    average_turn_score = None
    if count_turn_score > 1:
        average_turn_score = round(sum_turn_score / (count_turn_score - 1), 2)
    elif count_turn_score == 1:
        average_turn_score = round(sum_turn_score, 2)

    close_db(conn)

    return str(average_turn_score) if average_turn_score is not None else "0"






def get_last_win_date(player_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT MAX(Matches.MatchDate) 
        FROM Matches 
        JOIN MatchStats ON Matches.MatchID = MatchStats.MatchID
        WHERE MatchStats.MatchWinnerPlayerID = ? AND MatchStats.PlayerID = ?
    ''', (player_id, player_id))

    last_win_date = cursor.fetchone()[0]

    close_db(conn)

    return last_win_date if last_win_date is not None else None


def get_player_rank(player_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT MatchWinnerPlayerID, COUNT(*) AS WinCount
        FROM MatchStats
        GROUP BY MatchWinnerPlayerID
        ORDER BY WinCount DESC
    ''')
    sorted_players = cursor.fetchall()

    rank = None
    for i, (sorted_player_id, _) in enumerate(sorted_players, start=1):
        if sorted_player_id == player_id:
            rank = i
            break

    close_db(conn)

    return rank
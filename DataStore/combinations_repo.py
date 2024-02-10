import sqlite3
from itertools import product
import ast
database_name = 'dpl_database.db'

def connect_db():
    return sqlite3.connect(database_name)


def close_db(conn):
    if conn:
        conn.close()




def create_checkout_combinations():
    conn = connect_db()
    cursor = conn.cursor()

    multipliers = [1, 2, 3]
    values = list(range(1, 21)) + [25]
    all_combinations = [(m, v) for m in multipliers for v in values if not (m == 3 and v == 25)]

    bogey_numbers = [169, 168, 166, 165, 163, 162, 159]


    for score in range(2, 170):

        if score in bogey_numbers:
            cursor.execute('''
                INSERT INTO Combinations (Score, Combinations) 
                VALUES (?, ?)
            ''', (score, str(((0, 0), (0, 0), (0, 0)))))
            continue

        valid_combination = None


        for num_darts in range(1, 4):
            for throw_combination in product(all_combinations, repeat=num_darts):
                if throw_combination[-1][0] == 2 and sum(m * v for m, v in throw_combination) == score:
                    valid_combination = tuple(throw_combination)
                    break
            if valid_combination is not None:
                break

        if valid_combination is not None:
            cursor.execute('''
                INSERT INTO Combinations (Score, Combinations) 
                VALUES (?, ?)
            ''', (score, str(valid_combination)))

    cursor.execute("CREATE INDEX IF NOT EXISTS idx_score ON Combinations (Score)")
    conn.commit()
    conn.close()


def get_winning_combinations(score):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    cursor.execute('''
        SELECT Combinations
        FROM Combinations
        WHERE Score = ?
    ''', (score,))

    combinations_strings = cursor.fetchall()
    conn.close()

    if combinations_strings:
        winning_combinations = [ast.literal_eval(combo[0]) for combo in combinations_strings]
        return winning_combinations[0]
    else:
        return None

def get_all_combinations():
    conn = sqlite3.connect(database_name)
    c = conn.cursor()
    c.execute("SELECT * FROM Combinations")
    combinations = c.fetchall()
    close_db(conn)
    return combinations
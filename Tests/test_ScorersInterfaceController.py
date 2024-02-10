from Controllers.ScorersInterfaceController import ScorersInterfaceController
from Controllers.MatchController import MatchController
from DataStore import combinations_repo
from DataStore import init_database
import random
import threading
import time
from Controllers.PlayerController import PlayerController
from Controllers.MatchController import MatchController

init = init_database.init_db()
thread = threading.Thread(target=combinations_repo.create_checkout_combinations())
time.sleep(5)

player_controller = PlayerController()
player_controller.create_players('John', 'Doe', 'Jane', 'Smith')

match_controller = MatchController()
match_controller.create_match("2024-10-18", "Arena", 3, 3, 100)


score_controller = ScorersInterfaceController()
score_controller.create_starting_scores()


def generate_random_inputs():
    multiplier = random.choice([0, 1, 2, 3])
    value = random.randint(0, 20)

    if multiplier != 0 or value != 0:
        is_bounce_out = False
        is_foul_out = False
        is_knock_out = False
    else:
        is_bounce_out = random.choice([True, False])
        is_foul_out = random.choice([True, False])
        is_knock_out = random.choice([True, False])

    return multiplier, value, is_bounce_out, is_foul_out, is_knock_out


while True:
    print("-----------------------------------------------------------------")

    player_number = "Player 1" if score_controller.is_player_one_turn else "Player 2"
    user_input = input(f"{player_number}, enter 'M' for multiplier and 'V' for value, or hit Enter to throw a random dart: ").strip()

    if user_input.lower() == 'm':
        multiplier = int(input("Enter multiplier (0, 1, 2, 3): "))
        value = int(input("Enter value (0-20): "))
    elif user_input.lower() == 'v':
        value = int(input("Enter value (0-20): "))
        multiplier = int(input("Enter multiplier (0, 1, 2, 3): "))
    else:
        multiplier, value, _, _, _ = generate_random_inputs()

    is_bounce_out = False if multiplier != 0 or value != 0 else random.choice([True, False])
    is_foul_out = False if multiplier != 0 or value != 0 else random.choice([True, False])
    is_knock_out = False if multiplier != 0 or value != 0 else random.choice([True, False])

    print(f"{player_number}'s input:")
    print("Multiplier:", multiplier)
    print("Value:", value)
    print("Bounce Out:", is_bounce_out)
    print("Foul Out:", is_foul_out)
    print("Knock Out:", is_knock_out)

    score_controller.update_game_state(multiplier, value, is_bounce_out, is_foul_out, is_knock_out)


from DataStore import init_database
from DataStore import combinations_repo
import random

init_database.init_db()
combinations_repo.create_checkout_combinations()

score = 190
throw_number = 1

while score > 0:
    input(f"Throw {throw_number}: Press Enter to throw a dart...")

    points_scored = random.randint(1, 60)
    score -= points_scored
    print(f"Scored {points_scored} points, new score: {score}")

    if score == 0:
        print("Congratulations! You've hit exactly zero. Game won!")
        break
    elif score < 0:
        print("Bust! Score went below zero. Game over.")
        break

    winning_combination = combinations_repo.get_winning_combinations(score)
    if winning_combination:
        print("Possible winning combinations for this score:")
        print(winning_combination)
    else:
        print(f"No winning combination for score {score}")

    throw_number += 1

print("------------------------------------------------------")

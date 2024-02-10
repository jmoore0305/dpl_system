from DataStore import init_database
from DataStore import matches_repo
from DataStore import match_stats_repo
import random

init_database.init_db()

player1_id = 3
player2_id = 4

for i in range(1, 2):
    # Modify the date format here to '%m/%d/%Y'
    match_date = "11/03/2023"
    location = "Location"
    game_type = "GameType"

    # Add the match and get the match ID
    matches_repo.add_match(match_date, location, game_type)
    match_id = matches_repo.get_last_match_id()

    average_turn_score1 = random.uniform(50, 150)
    number_of_180s1 = 1
    match_winner_player_id = player1_id if random.random() < 0.5 else player2_id  # Randomly select a winner

    # Add match stats for player one
    match_stats_repo.add_match_stats(player1_id, match_id, average_turn_score1, number_of_180s1, match_winner_player_id)

    average_turn_score2 = random.uniform(50, 150)
    number_of_180s2 = 1
    # Use the same match_winner_player_id for player two
    match_stats_repo.add_match_stats(player2_id, match_id, average_turn_score2, number_of_180s2, match_winner_player_id)

matches_repo.print_all_matches()
match_stats_repo.print_all_match_stats()

print("--------------------------------------------------------------------")
print("Player 2 total number of 180's for current season: " + str(matches_repo.get_total_180s_in_season(player2_id)))
print("--------------------------------------------------------------------")

print("--------------------------------------------------------------------")
print("Player 2 average turn score for current season: " + str(matches_repo.get_average_turn_score_in_season(player2_id)))
print("--------------------------------------------------------------------")

print("--------------------------------------------------------------------")
print("Player 2 last win: " + str(matches_repo.get_last_win_date(player2_id)))
print("--------------------------------------------------------------------")

print("--------------------------------------------------------------------")
print("Player 2 rank : " + str(matches_repo.get_player_rank(player2_id)))
print("--------------------------------------------------------------------")

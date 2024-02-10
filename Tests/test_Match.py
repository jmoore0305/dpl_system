from Model.Match import Match
from DataStore import init_database

init_database.init_db()

match = Match()

match.set_match_date('2023-11-15')
match.set_location('Los Angeles')
match.set_starting_score(501)
match.add_match()

print("----------------------------------------------------------------")
print("Match Date:", match.get_match_date())
print("Location:", match.get_location())
print("Starting Score:", match.get_starting_score())
print("----------------------------------------------------------------")

match.set_match_date('2023-11-16')
match.set_location('New York')
match.set_match_winner_player_id(1)
match.update_match()

print("Match Date:", match.get_match_date())
print("Location:", match.get_location())
print("Match Winner Player ID:", match.get_match_winner_player_id())
print("----------------------------------------------------------------")

match.set_match_date('2023-01-16')
match.set_location('Los Angeles')
match.set_number_of_180s(3)
match.set_match_winner_player_id(2)
match.update_match()

print("Match Date:", match.get_match_date())
print("Location:", match.get_location())
print("Match Winner Player ID:", match.get_match_winner_player_id())
print("----------------------------------------------------------------")

match.set_lowest_turn_score(15)
match.set_average_turn_score(45)
match.set_highest_turn_score(50)
match.set_match_winner_player_id(3)
match.update_match()

print("Match Date:", match.get_match_date())
print("Location:", match.get_location())
print("Match Winner Player ID:", match.get_match_winner_player_id())
print("----------------------------------------------------------------")

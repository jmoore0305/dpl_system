from DataStore import init_database
from DataStore import dart_throw_history_repo

# You may want to delete the database after each run
init_database.init_db()

# Replace this with player_id
player_id = 1  # Example player ID

# Use the updated add_throw function with player_id, score, multiplier, value, is_bounce_out, is_knock_out, is_foul_out
dart_throw_history_repo.add_throw(player_id, 50, 1, 50, False, True, False)
dart_throw_history_repo.add_throw(player_id, 4, 1, 4, False, True, False)
dart_throw_history_repo.add_throw(player_id, 1, 1, 1, False, True, False)
dart_throw_history_repo.add_throw(player_id, 7, 1, 7, False, True, False)
dart_throw_history_repo.add_throw(player_id, 5, 1, 5, False, True, False)
dart_throw_history_repo.add_throw(player_id, 0, 1, 0, False, True, False)
dart_throw_history_repo.add_throw(player_id, 48, 1, 48, False, True, False)
dart_throw_history_repo.add_throw(player_id, 7, 1, 7, False, True, False)
dart_throw_history_repo.add_throw(player_id, 5, 1, 5, False, True, False)
dart_throw_history_repo.add_throw(player_id, 9, 1, 9, False, True, False)
dart_throw_history_repo.add_throw(player_id, 2, 1, 2, False, True, False)
dart_throw_history_repo.add_throw(player_id, 15, 1, 15, False, True, False)
dart_throw_history_repo.add_throw(player_id, 18, 1, 18, False, True, False)
dart_throw_history_repo.add_throw(player_id, 45, 1, 45, False, True, False)
dart_throw_history_repo.add_throw(player_id, 7, 1, 7, False, True, False)
dart_throw_history_repo.add_throw(player_id, 43, 1, 43, False, True, False)
dart_throw_history_repo.add_throw(player_id, 44, 1, 44, False, True, False)
dart_throw_history_repo.add_throw(player_id, 1, 1, 1, False, True, False)
dart_throw_history_repo.add_throw(player_id, 4, 1, 4, False, True, False)
dart_throw_history_repo.add_throw(player_id, 67, 1, 67, False, True, False)

all_throws_p = dart_throw_history_repo.get_all_throws_for_player(player_id)  # Use get_all_throws_for_player
all_throws = dart_throw_history_repo.get_last_ten_throws_for_all()

print(all_throws)








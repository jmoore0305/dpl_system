from DataStore import init_database
from DataStore import match_stats_repo

init_database.init_db()

match_id = 1
player1_id = 1
player2_id = 2

match_stats_repo.add_match_stats(player1_id, match_id, 100.5, 3, 1)
match_stats_repo.add_match_stats(player2_id, match_id, 95.4, 4, 2)

match_stats_repo.print_all_match_stats()

last_id = match_stats_repo.get_last_stats_id()
print("Last ID:", last_id)


match_winner_id = player1_id
match_stats_repo.update_match_stats(player1_id, match_id, match_winner_player_id=match_winner_id)

match_stats_repo.print_all_match_stats()

match_stats_repo.delete_match_stats_by_id(last_id)

deleted_stats_check = match_stats_repo.get_match_stats_by_id(last_id)
print(deleted_stats_check)

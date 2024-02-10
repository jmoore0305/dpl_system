from DataStore import init_database
from DataStore import player_repo

init_database.init_db()

player_repo.add_player("John", "Doe")
player_repo.add_player("Jane", "Smith")

second_to_last_id = player_repo.get_player_one_id()
last_id = player_repo.get_player_two_id()

player_repo.update_player(second_to_last_id, last_name="Ropper")
player_repo.update_player(last_id, last_name="Amami")

print("Player One ID:", second_to_last_id)
print("Player Two ID:", last_id)

player_repo.print_all_players()

list = player_repo.get_list()

print(list)
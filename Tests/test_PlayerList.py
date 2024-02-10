from Model.PlayerList import PlayerList
from DataStore import init_database

init_database.init_db()

player_list = PlayerList()
player_list.load_player_list()

#player_list.add_player("John", "Doe")
player_list.add_player("Jane", "Smith")

#player_list.remove_player("John", "Doe")

players_list = player_list.get_player_list()

player_list.print_players()
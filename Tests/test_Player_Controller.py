from Controllers.PlayerController import PlayerController
from DataStore import init_database


init = init_database.init_db()
player_controller = PlayerController()

player_controller.create_players('John', 'Doe', 'Jane', 'Smith')

print("Player One:", player_controller.get_player_one().get_first_name(), player_controller.get_player_one().get_last_name())
print("Player Two:", player_controller.get_player_two().get_first_name(), player_controller.get_player_two().get_last_name())
print("Do Players Exist:", player_controller.do_players_exist())

player_controller.update_players('Mike', 'Tyson', 'Serena', 'Williams')

print("Player One Updated:", player_controller.get_player_one().get_first_name(), player_controller.get_player_one().get_last_name())
print("Player Two Updated:", player_controller.get_player_two().get_first_name(), player_controller.get_player_two().get_last_name())
print("Do Players Exist After Update:", player_controller.do_players_exist())
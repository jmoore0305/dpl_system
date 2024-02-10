from Controllers.MaintainPlayersController import MaintainPlayersController
from DataStore import init_database


init = init_database.init_db()
controller1 = MaintainPlayersController()

player_list_exist = controller1.does_player_list_exist()

if player_list_exist:
    pass
else:
    controller1.load_player_list()



controller1.add_player_to_list("Alice", "Johnson")

controller1.add_player_to_list("Bob", "Smith")


controller1.add_player_to_list("Alice", "Johnson")


controller1.remove_player_from_list("Alice", "Johnson")

controller2 = MaintainPlayersController()
print("Is controller1 the same as controller2?", controller1 is controller2)

print("Players in the list (via controller2):")
controller2.PlayerList.print_players()


list = controller1.get_player_list()

print(list)
from Model.Player import Player
from DataStore import init_database, player_repo

if __name__ == '__main__':
    init_database.init_db()


    player_one = Player()

    player_two = Player()

    player_one.set_first_name("Justin")
    player_one.set_last_name("Moore")
    player_one.add_player()

    player_two.set_first_name("Michelle")
    player_two.set_last_name("Patel")
    player_two.add_player()



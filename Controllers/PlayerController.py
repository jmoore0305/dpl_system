from Model.Player import Player

class PlayerController:
    my_instance = None  #var for storing the singleton instance.

    def __new__(cls):
        if not cls.my_instance:
            cls.my_instance = super(PlayerController, cls).__new__(cls)
            cls.my_instance.PlayerOne = Player()
            cls.my_instance.PlayerTwo = Player()
            cls.my_instance.players_exist: bool = False
        return cls.my_instance

    def get_player_one(self):
        return self.PlayerOne

    def get_player_two(self):
        return self.PlayerTwo

    def do_players_exist(self):
        return self.players_exist

    def create_players(self, player_one_fname, player_one_lname, player_two_fname, player_two_lname):
        self.PlayerOne.set_first_name(player_one_fname)
        self.PlayerOne.set_last_name(player_one_lname)
        self.PlayerOne.add_player()
        self.PlayerTwo.set_first_name(player_two_fname)
        self.PlayerTwo.set_last_name(player_two_lname)
        self.PlayerTwo.add_player()
        self.players_exist = True

    def update_players(self, player_one_fname, player_one_lname, player_two_fname, player_two_lname):
        self.PlayerOne.set_first_name(player_one_fname)
        self.PlayerOne.set_last_name(player_one_lname)
        self.PlayerOne.update_player_name()
        self.PlayerTwo.set_first_name(player_two_fname)
        self.PlayerTwo.set_last_name(player_two_lname)
        self.PlayerTwo.update_player_name()















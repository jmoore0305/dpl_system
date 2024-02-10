from Model.PlayerList import PlayerList

class MaintainPlayersController:
    my_instance = None  #var for storing the singleton instance.

    def __new__(cls):
        if not cls.my_instance:
            cls.my_instance = super(MaintainPlayersController, cls).__new__(cls)
            cls.my_instance.PlayerList = PlayerList()
            cls.my_instance.playerList_exist: bool = False
        return cls.my_instance

    def does_player_list_exist(self):
        return self.my_instance.playerList_exist

    def load_player_list(self):
        self.my_instance.PlayerList.load_player_list()
        self.my_instance.playerList_exist = True

    def add_player_to_list(self, first_name, last_name):
        self.my_instance.PlayerList.add_player(first_name, last_name)

    def remove_player_from_list(self, first_name, last_name):
        self.my_instance.PlayerList.remove_player(first_name, last_name)

    def get_player_list(self):
        return self.my_instance.PlayerList.get_player_list()
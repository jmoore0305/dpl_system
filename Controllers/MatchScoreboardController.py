from Controllers.PlayerController import PlayerController
class MatchScoreboardController:
    my_instance = None  #var for storing the singleton instance.

    def __new__(cls):
        if not cls.my_instance:
            cls.my_instance = super(MatchScoreboardController, cls).__new__(cls)
            player_controller = PlayerController()
            cls.my_instance.PlayerOne = player_controller.get_player_one()
            cls.my_instance.PlayerTwo = player_controller.get_player_two()
        return cls.my_instance


    def read_info(self):
        p1_first_name = self.PlayerOne.get_first_name()
        p1_last_name = self.PlayerOne.get_last_name()
        p2_first_name = self.PlayerTwo.get_first_name()
        p2_last_name = self.PlayerTwo.get_last_name()


        info_list = [
            p1_first_name,
            p1_last_name,
            p2_first_name,
            p2_last_name,
        ]

        return info_list
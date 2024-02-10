from Controllers.PlayerController import PlayerController
from DataStore import match_stats_repo, matches_repo, player_repo, dart_throw_history_repo


class Match:
    def __init__(self):
        self.match_winner_player_id = None
        self.location = None
        self.match_date = None
        self.num_of_leg = None
        self.total_matches = None
        self.starting_score = None
        self.lowest_turn_score = None
        self.average_turn_score = None
        self.highest_turn_score = None
        self.number_of_180s = None
        player_controller = PlayerController()
        self.PlayerOne = player_controller.get_player_one()
        self.PlayerTwo = player_controller.get_player_two()

    def get_match_winner_player_id(self):
        return self.match_winner_player_id

    def set_match_winner_player_id(self, value):
        self.match_winner_player_id = value

    def delete_last_dart(self):
        dart_throw_history_repo.delete_last_throw()

    def get_last_ten_throws_for_all(self):
        return dart_throw_history_repo.get_last_ten_throws_for_all()

    def is_player_one_throw_last_dart(self, player_one_first_name, player_one_last_name):
        id = dart_throw_history_repo.get_last_entry_player_id()
        player_id = player_repo.get_player_id_by_name(player_one_first_name, player_one_last_name)
        if id == player_id:
            return True
        else:
            return False

    def get_match_winner_name(self):
        return self.match_winner_name

    def set_match_winner_name(self, match_winner_name):
        self.match_winner_name = match_winner_name

    def get_match_date(self):
        return self.match_date

    def set_match_date(self, match_date):
        self.match_date = match_date
        print("Match Date Format:", type(self.match_date), "-", self.match_date)

    def get_location(self):
        return self.location

    def set_location(self, location):
        self.location = location

    def get_num_of_leg(self):
        return self.num_of_leg

    def set_num_of_leg(self, num_of_leg):
        self.num_of_leg = num_of_leg

    def get_total_matches(self):
        return self.total_matches

    def set_total_matches(self, total_matches):
        self.total_matches = total_matches

    def get_starting_score(self):
        return self.starting_score

    def set_starting_score(self, starting_score):
        self.starting_score = starting_score

    def get_lowest_turn_score(self):
        return self.lowest_turn_score

    def set_lowest_turn_score(self, lowest_turn_score):
        self.lowest_turn_score = lowest_turn_score

    def get_average_turn_score(self):
        return self.average_turn_score

    def set_average_turn_score(self, average_turn_score):
        self.average_turn_score = average_turn_score

    def get_highest_turn_score(self):
        return self.highest_turn_score

    def set_highest_turn_score(self, highest_turn_score):
        self.highest_turn_score = highest_turn_score

    def get_number_of_180s(self):
        return self.number_of_180s

    def set_number_of_180s(self, number_of_180s):
        self.number_of_180s = number_of_180s

    def add_match(self):
        player_one_id = player_repo.get_player_id_by_name(self.PlayerOne.get_first_name(),
                                                          self.PlayerOne.get_last_name())
        player_two_id = player_repo.get_player_id_by_name(self.PlayerTwo.get_first_name(),
                                                          self.PlayerTwo.get_last_name())
        print("player_one_id = " + str(player_one_id))
        print("player_two_id = " + str(player_two_id))

        matches_repo.add_match(self.match_date, self.location, self.starting_score)
        match_id = matches_repo.get_last_match_id()


        match_stats_repo.add_match_stats(player_one_id, match_id, 0, 0,
                                         None)

        match_stats_repo.add_match_stats(player_two_id, match_id, 0, 0,
                                         None)










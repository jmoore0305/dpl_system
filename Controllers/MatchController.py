from Model.Match import Match

class MatchController:
    my_instance = None  #var for storing the singleton instance.

    def __new__(cls):
        if not cls.my_instance:
            cls.my_instance = super(MatchController, cls).__new__(cls)
            cls.my_instance.Match = Match()
            cls.my_instance.match_exist: bool = False
        return cls.my_instance

    def get_match(self):
        return self.Match
    def does_match_exist(self):
        return self.match_exist


    def create_match(self, match_date, location, num_of_leg, total_matches, starting_score):
        self.Match.set_match_date(match_date)
        self.Match.set_location(location)
        self.Match.set_num_of_leg(int(num_of_leg))
        self.Match.set_total_matches(int(total_matches))
        self.Match.set_starting_score(int(starting_score))
        self.Match.add_match()
        self.match_exist = True

    def update_match(self, match_date, location, num_of_leg, total_matches, starting_score):
        self.Match.set_match_date(match_date)
        self.Match.set_location(location)
        self.Match.set_num_of_leg(int(num_of_leg))
        self.Match.set_total_matches(int(total_matches))
        self.Match.set_starting_score(int(starting_score))
        self.Match.update_match()


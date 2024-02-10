from Controllers.MatchController import MatchController
from Controllers.PlayerController import PlayerController
import time
from DataStore import match_stats_repo, matches_repo, player_repo

from DataStore import combinations_repo


class ScorersInterfaceController:
    my_instance = None

    def __init__(self):
        self.is_player_one_winner = None
        match_controller = MatchController()
        self.Match = match_controller.get_match()

    def __new__(cls):
        if cls.my_instance is None:
            cls.my_instance = super(ScorersInterfaceController, cls).__new__(cls)
            player_controller = PlayerController()
            cls.my_instance.PlayerOne = player_controller.get_player_one()
            cls.my_instance.PlayerTwo = player_controller.get_player_two()
            cls.my_instance.scorers_interface_exist = False
            cls.my_instance.is_player_one_turn = True
        return cls.my_instance


    def does_scorers_interface_exist(self):
        return self.scorers_interface_exist

    def create_starting_scores(self):
        starting_score = self.Match.get_starting_score()
        self.PlayerOne.set_starting_score(starting_score)
        self.PlayerTwo.set_starting_score(starting_score)
        self.scorers_interface_exist = True


    def mark_as_knock_off(self, dart_number):
        print("dart number = " + str(dart_number))
        throws = self.Match.get_last_ten_throws_for_all()
        print("printing last ten throws")
        print(throws)


        is_player_one_throw_last_dart = self.Match.is_player_one_throw_last_dart(self.PlayerOne.get_first_name(), self.PlayerOne.get_last_name())
        print("did player one throw the last dart? = " + str(is_player_one_throw_last_dart))
        if is_player_one_throw_last_dart and self.is_player_one_turn:
            print("player one's turn to mark as knock off")
            self.PlayerOne.update_specific_dart_throw(dart_number)

        elif not is_player_one_throw_last_dart and not self.is_player_one_turn:
            print("player two's turn to mark as knock off")
            self.PlayerOne.update_specific_dart_throw(dart_number)

        else:
            pass

        print("dart number = " + str(dart_number))
        throws = self.Match.get_last_ten_throws_for_all()
        print("printing last ten throws")
        print(throws)




    def redo_last_throw(self):
        is_player_one_throw_last_dart = self.Match.is_player_one_throw_last_dart(self.PlayerOne.get_first_name(), self.PlayerOne.get_last_name())
        print("did player one throw the last dart? = " + str(is_player_one_throw_last_dart))
        if is_player_one_throw_last_dart and self.is_player_one_turn:
            print("player one's turn")
            self.PlayerOne.remove_last_score()
            self.PlayerOne.decrement_turn_count()
            self.Match.delete_last_dart()
        elif not is_player_one_throw_last_dart and not self.is_player_one_turn:
            print("player two's turn")
            self.PlayerTwo.remove_last_score()
            self.PlayerTwo.decrement_turn_count()
            self.Match.delete_last_dart()
        else:
            pass


    def update_game_state(self, multiplier, value, is_bounce_out, is_foul_out, is_knock_out):

        if self.is_player_one_turn:
            self.PlayerOne.increment_turn_count()
            self.PlayerOne.increment_leg_darts_thrown()
            is_valid_score = self.PlayerOne.update_score(True, multiplier, value, is_bounce_out, is_foul_out, is_knock_out)

            self.check_on_track_for_perfect()

            print("-------------------- Adding throw score to turn score list for player one --------------------")
            if is_valid_score:
                self.PlayerOne.add_turn_score(multiplier * value)
            else:
                self.PlayerOne.add_turn_score(0)
            print("----------------------------------------------------------------------------------------------")
            print("player one current score: " + str(self.PlayerOne.get_score()))


            if self.PlayerOne.get_score() >= 2 and self.PlayerOne.get_score() <= 170:
                print("-------------------- winning combo --------------------")
                print("player one score to get winning combo = " + str(self.PlayerOne.get_score()))
                winning_combination = combinations_repo.get_winning_combinations(self.PlayerOne.get_score())
                self.PlayerOne.set_winning_combination(winning_combination)
                for combo in winning_combination:
                    print(combo)

                print("------------------------------------------------------")

            self.PlayerOne.update_dart_throws()

            if self.PlayerOne.get_turn_count() == 3:
                is_180 = self.PlayerOne.check_if_180()
                print("printing is_180 in scorers interfac: " + str(is_180))
                if is_180:
                    self.PlayerOne.increment_num_180s()
                print("-------------------- printing turn stats for player one ------------------------")
                print("Lowest Turn Score = " + str(self.PlayerOne.get_lowest_turn_score()))
                print("Average Turn Score = " + str(self.PlayerOne.get_average_turn_score()))
                print("Highest Turn Score = " + str(self.PlayerOne.get_highest_turn_score()))
                print("Number of 180's in Match = " + str(self.PlayerOne.get_num_180s()))
                print("-----------------------------------------------------------------")
                self.is_player_one_turn = False
                self.PlayerOne.set_turn_count(0)
                print(
                    "----------------Player one didn't win leg. Adding turn stats to leg scores list for player one ------------------------")
                self.PlayerOne.add_turn_scores_to_legs_list()
                print("-----------------------------------------------------------------")
                self.PlayerOne.clear_turn_scores()

        else:
            self.PlayerTwo.increment_turn_count()
            self.PlayerOne.increment_leg_darts_thrown()
            is_valid_score = self.PlayerTwo.update_score(False, multiplier, value, is_bounce_out, is_foul_out, is_knock_out)

            self.check_on_track_for_perfect()

            print("-------------------- Adding throw score to turn score list for player two --------------------")
            if is_valid_score:
                self.PlayerTwo.add_turn_score(multiplier * value)
            else:
                self.PlayerTwo.add_turn_score(0)
            print("----------------------------------------------------------------------------------------------")
            print("player two current score: " + str(self.PlayerTwo.get_score()))


            if self.PlayerTwo.get_score() >= 2 and self.PlayerTwo.get_score() <= 170:
                print("-------------------- winning combo --------------------")

                winning_combination = combinations_repo.get_winning_combinations(self.PlayerTwo.get_score())
                self.PlayerTwo.set_winning_combination(winning_combination)
                for combo in winning_combination:
                    print(combo)
                print("------------------------------------------------------")

            self.PlayerTwo.update_dart_throws()

            if self.PlayerTwo.get_turn_count() == 3:
                is_180 = self.PlayerTwo.check_if_180()
                if is_180:
                    self.PlayerTwo.increment_num_180s()
                print("-------------------- printing turn stats for player two ------------------------")
                print("Lowest Turn Score = " + str(self.PlayerTwo.get_lowest_turn_score()))
                print("Average Turn Score = " + str(self.PlayerTwo.get_average_turn_score()))
                print("Highest Turn Score = " + str(self.PlayerTwo.get_highest_turn_score()))
                print("Number of 180's in Match = " + str(self.PlayerTwo.get_num_180s()))
                print("-----------------------------------------------------------------")
                self.is_player_one_turn = True
                self.PlayerTwo.set_turn_count(0)
                print("----------------Player two didn't win leg. Adding turn stats to leg scores list for player two ------------------------")
                self.PlayerTwo.add_turn_scores_to_legs_list()
                print("-----------------------------------------------------------------")
                self.PlayerTwo.clear_turn_scores()


        if self.PlayerOne.get_won_leg():
            print("--------Player one won leg. Adding turn stats to leg scores list for player one---------------")
            self.PlayerOne.add_turn_scores_to_legs_list()
            print("-----------------------------------------------------------------")

            print("player one wins, leg is over ****************************************")
            self.PlayerOne.increment_legs_won()

        if self.PlayerTwo.get_won_leg():
            print("--------Player two won leg. Adding turn stats to leg scores list for player two----------------")
            self.PlayerOne.add_turn_scores_to_legs_list()
            print("-----------------------------------------------------------------")

            print("player two wins, leg is over ****************************************")
            self.PlayerTwo.increment_legs_won()



        if self.PlayerOne.get_won_leg() or self.PlayerTwo.get_won_leg():
            self.PlayerOne.clear_turn_scores()
            self.PlayerTwo.clear_turn_scores()
            self.PlayerOne.reset_leg_darts_thrown()
            self.PlayerTwo.reset_leg_darts_thrown()
            self.PlayerOne.set_num_180s(0)
            self.PlayerTwo.set_num_180s(0)
            self.PlayerOne.set_starting_score(self.Match.get_starting_score())
            self.PlayerTwo.set_starting_score(self.Match.get_starting_score())
            self.is_player_one_turn = True
            self.PlayerOne.set_won_leg(False)
            self.PlayerTwo.set_won_leg(False)
            self.PlayerOne.set_turn_count(0)
            self.PlayerTwo.set_turn_count(0)
            self.PlayerOne.clear_winning_combinations()
            self.PlayerTwo.clear_winning_combinations()
            self.PlayerOne.clear_dart_throws()
            self.PlayerOne.clear_dart_throws()
            print("-------------------- Adding leg scores to match scores list for player one ------------------------")
            self.PlayerOne.add_scores_to_matches_list()
            self.PlayerOne.print_matches_list()
            print("-----------------------------------------------------------------")
            print("-------------------- Adding leg scores to match scores list for player two ------------------------")
            self.PlayerTwo.add_scores_to_matches_list()
            print("-----------------------------------------------------------------")
            self.PlayerOne.clear_leg_scores()
            self.PlayerTwo.clear_leg_scores()

        print("player one legs won: " + str(self.PlayerOne.get_legs_won()))
        print("player two legs won: " + str(self.PlayerTwo.get_legs_won()))

        print("//////////////////////////////////////////////////////////////////////////")
        #print("//////////////////////////////////////////////////////////////////////////")
        #print("//////////////////////////////////////////////////////////////////////////")
        #print("//////////////////////////////////////////////////////////////////////////")
        #print("//////////////////////////////////////////////////////////////////////////")
        #print("//////////////////////////////////////////////////////////////////////////")
        #print("//////////////////////////////////////////////////////////////////////////")
        #print("//////////////////////////////////////////////////////////////////////////")


        if self.PlayerOne.get_legs_won() > self.Match.get_num_of_leg() / 2:
            self.is_player_one_winner = True
            self.PlayerOne.increment_matches_won()
            print("player one matches won: " + str(self.PlayerOne.get_matches_won()))


        if self.PlayerTwo.get_legs_won() > self.Match.get_num_of_leg() / 2:
            self.is_player_one_winner = False
            self.PlayerTwo.increment_matches_won()
            print("player two matches won: " + str(self.PlayerTwo.get_matches_won()))



        if self.PlayerOne.get_legs_won() > self.Match.get_num_of_leg() / 2 or self.PlayerTwo.get_legs_won() > self.Match.get_num_of_leg() / 2:
            player_one_id = player_repo.get_player_id_by_name(self.PlayerOne.get_first_name(), self.PlayerOne.get_last_name())
            player_two_id = player_repo.get_player_id_by_name(self.PlayerTwo.get_first_name(), self.PlayerTwo.get_last_name())

            if self.is_player_one_winner:
                self.PlayerOne.add_match_list_to_db(True, True, player_one_id, player_two_id)
                self.PlayerTwo.add_match_list_to_db(True, False, player_one_id, player_two_id)
            else:
                self.PlayerOne.add_match_list_to_db(False, True, player_one_id, player_two_id)
                self.PlayerTwo.add_match_list_to_db(False, False, player_one_id, player_two_id)

            self.PlayerOne.set_legs_won(0)
            self.PlayerTwo.set_legs_won(0)
            self.PlayerOne.set_num_180s(0)
            self.PlayerTwo.set_num_180s(0)
            self.PlayerOne.clear_match_scores()
            self.PlayerTwo.clear_match_scores()
            match_stats_repo.print_all_match_stats()
            self.PlayerOne.clear_match_scores()
            self.PlayerTwo.clear_match_scores()
            self.is_player_one_winner = None

            if ((self.PlayerOne.get_matches_won() < self.Match.get_total_matches() / 2 or self.PlayerTwo.get_matches_won() < self.Match.get_total_matches() / 2) and
                    self.PlayerOne.get_matches_won() != self.Match.get_total_matches() and self.PlayerTwo.get_matches_won() != self.Match.get_total_matches()):
                print("player one matches won: " + str(self.PlayerOne.get_matches_won()))

                print("total matches: " + str(self.Match.get_total_matches()))

                print("player two matches won: " + str(self.PlayerTwo.get_matches_won()))
                self.Match.add_match()
            else:
                if self.PlayerOne.get_matches_won() > self.Match.get_total_matches() / 2:
                    self.PlayerOne.clear_dart_throws()
                    self.PlayerTwo.clear_dart_throws()
                    print("PLAYER ONE WINS")
                    print("LOAD THE WELCOME SCREEN")
                    time.sleep(10)
                    exit(0)
                else:
                    self.PlayerOne.clear_dart_throws()
                    self.PlayerTwo.clear_dart_throws()
                    print("PLAYER TWO WINS")
                    print("LOAD THE WELCOME SCREEN")
                    time.sleep(3)
                    exit(0)

    def check_on_track_for_perfect(self):
        print("check_on_track_for_perfect")
        min_throws = 0
        print("is_player_one_turn: " + str(self.is_player_one_turn))
        if self.is_player_one_turn: # confirm this runs before current player changes
            player_reference = self.PlayerOne
            print("playerOne")
        else:
            player_reference = self.PlayerTwo
            print("playerTwo")

        if not(player_reference.get_on_track_for_perfect()):
            print("if not(player_reference.get_on_track_for_perfect())")
            return

        current_leg_value = int(self.Match.get_starting_score())
        if current_leg_value == 801:
            min_throws = 15
        if current_leg_value == 501:
            min_throws = 9
        if current_leg_value == 301:
            min_throws = 6

        print("current_leg_value: " + str(current_leg_value))

        player_remaining_score = player_reference.get_score()
        print("player_remaining_score: " + str(player_remaining_score))
        player_num_darts_thrown = player_reference.get_leg_darts_thrown()
        print("player_num_darts_thrown: " + str(player_num_darts_thrown))

        min_possible_throws = min_throws - player_num_darts_thrown
        print("min_possible_throws: " + str(min_possible_throws))

        temp_score = player_remaining_score
        print("temp_score: " + str(temp_score))

        if min_possible_throws <= 0:
            player_reference.set_on_track_for_perfect(False)
            print("False, min_possible_throws <= 0")

        if player_remaining_score % 2 == 0 and min_possible_throws == 1:
            player_reference.set_on_track_for_perfect(False)
            print("False, player_remaining_score is even and min_possible_throws is 1")
            return

        largest_valid_odd = 0
        valid_odds = [57, 51, 45, 39, 33, 27, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]

        for i in valid_odds:
            if player_remaining_score - i >= 2:
                largest_valid_odd = i
                print("largest_valid_odd: " + str(largest_valid_odd))
                break

        temp_score -= largest_valid_odd
        print("temp_score - largest_valid_odd: " + str(temp_score))

        imaginary_min_possible_throws = min_possible_throws - 1
        print("imaginary_min_possible_throws: " + str(imaginary_min_possible_throws))

        if 40 >= temp_score >= 2:
            print("True, 40 >= temp_score >= 2")
            return

        min_throws_to_win = int(temp_score/60)
        print("min_throws_to_win: " + str(min_throws_to_win))
        remainder = temp_score % 60
        print("remainder: " + str(remainder))

        if 40 >= remainder >=2:
            min_throws_to_win += 1
            print("min_throws_to_win += 1")
        else:
            min_throws_to_win += 2
            print("min_throws_to_win += 2")

        if min_throws_to_win > imaginary_min_possible_throws:
            player_reference.set_on_track_for_perfect(False)
            print("False, min_throws_to_win > imaginary_min_possible_throws")
            print("min_throws_to_win: " + str(min_throws_to_win))
            print("imaginary_min_possible_throws: " + str(imaginary_min_possible_throws))

        print("reached end of check_on_track_for_perfect_score")
        return
        # We''ll increment this every time we edit temp_score in a way that would emulate a dart throw




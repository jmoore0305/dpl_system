from DataStore import player_repo, dart_throw_history_repo, combinations_repo, match_stats_repo, matches_repo


class Player():
    def __init__(self):
        self.processed_throws = []
        self.winning_combination = ''
        self.value = 0
        self.multiplier = 0
        self.matches_list = []
        self.leg_scores = None
        self.leg_scores_tuple = None
        self.highest_turn_score = None
        self.lowest_turn_score = None
        self.average_turn_score = None
        self.PlayerID = None
        self.first_name = None
        self.last_name = None
        self.old_first_name = None
        self.old_last_name = None
        self.current_score = 0
        self.legs_won = 0
        self.turn_count = 0
        self.won_leg = None
        self.matches_won = 0
        self.turn_score_list = []
        self.leg_score_list = []
        self.number_of_180s = 0
        
        self.on_track_for_perfect = True
        self.leg_darts_thrown = 0

    def get_on_track_for_perfect(self):
        return self.on_track_for_perfect
    
    def set_on_track_for_perfect(self, is_on_track):
        self.on_track_for_perfect = is_on_track

    def increment_leg_darts_thrown(self):
        self.leg_darts_thrown += 1

    def reset_leg_darts_thrown(self):
        self.leg_darts_thrown = 0

    def get_leg_darts_thrown(self):
        return self.leg_darts_thrown

    def remove_last_score(self):
        if self.turn_score_list:
            removed_score = self.turn_score_list.pop()
            print("Removed score: " + str(removed_score))
        else:
            print("No scores to remove.")

        print(self.turn_score_list)
    def add_turn_score(self, score):
        self.turn_score_list.append(score)
        print(self.turn_score_list)

    def check_if_180(self):
        if len(self.turn_score_list) >= 3:
            total_score = sum(self.turn_score_list[-3:])
            return total_score == 180
        else:
            return False

    def remove_last_turn_score(self):
        if self.turn_score_list:
            self.turn_score_list.pop()

    def get_average_turn_score(self):
        if not self.turn_score_list:
            return 0

        total_score = sum(self.turn_score_list)
        number_of_scores = len(self.turn_score_list)
        average_score = total_score / number_of_scores
        self.average_turn_score = round(average_score, 2)
        return self.average_turn_score

    def get_lowest_turn_score(self):
        if not self.turn_score_list:
            return None
        self.lowest_turn_score = min(self.turn_score_list)
        return self.lowest_turn_score

    def get_highest_turn_score(self):
        if not self.turn_score_list:
            return None
        self.highest_turn_score = max(self.turn_score_list)
        return self.highest_turn_score

    def increment_num_180s(self):
        self.number_of_180s += 1






    def add_turn_scores_to_legs_list(self):
        average_turn_score = self.get_average_turn_score()
        number_of_180s_turns = self.get_num_180s()

        if not hasattr(self, 'leg_scores') or self.leg_scores is None:
            self.leg_scores = []

        score_turn = (average_turn_score, number_of_180s_turns)
        self.leg_scores.append(score_turn)

        print(self.leg_scores)






    def clear_turn_scores(self):
        self.turn_score_list = []


    def clear_leg_scores(self):
        self.leg_scores = []


    def clear_match_scores(self):
        self.matches_list = []

    def print_matches_list(self):
        print("-----------printing matches list----------------")
        print(self.matches_list)
        print("------------------------------------------------")
    def add_scores_to_matches_list(self):
        if not hasattr(self, 'leg_scores') or not self.leg_scores:
            print("No leg scores to calculate from.")
            return

        total_average_score = sum(score_turn[0] for score_turn in self.leg_scores) / len(self.leg_scores)
        total_180s = sum(score_turn[1] for score_turn in self.leg_scores)

        print("printing total average score to put in matches list: " + str(total_average_score))
        print("printing total 180s to put in matches list: " + str(total_180s))

        self.matches_list.append([total_average_score, total_180s])










    def add_match_list_to_db(self, is_player_one_winner, is_player_one_calling, player_one_id, player_two_id):
        match_id = matches_repo.get_last_match_id()

        total_score_sum = 0
        total_180s_count = 0

        for score_turn in self.matches_list:
            total_score_sum += score_turn[0]
            total_180s_count += score_turn[1]

        if self.matches_list:
            average_score = total_score_sum / len(self.matches_list)
        else:
            average_score = 0

        print(f"Total Average Score: {average_score}, Total 180s: {total_180s_count}")



        if is_player_one_winner and is_player_one_calling:
            match_stats_repo.update_match_stats(player_one_id, match_id, average_turn_score=average_score,
                                                number_of_180s=total_180s_count,
                                                match_winner_player_id=player_one_id)
        if not is_player_one_winner and is_player_one_calling:
            match_stats_repo.update_match_stats(player_one_id, match_id, average_turn_score=average_score,
                                                number_of_180s=total_180s_count,
                                                match_winner_player_id=player_two_id)




        if is_player_one_winner and not is_player_one_calling:
            match_stats_repo.update_match_stats(player_two_id, match_id, average_turn_score=average_score,
                                                number_of_180s=total_180s_count,
                                                match_winner_player_id=player_one_id)
        if not is_player_one_winner and not is_player_one_calling:
            match_stats_repo.update_match_stats(player_two_id, match_id, average_turn_score=average_score,
                                                number_of_180s=total_180s_count,
                                                match_winner_player_id=player_two_id)





    def get_match_scores(self):
        return self.matches_list


    def get_num_180s(self):
        return self.number_of_180s

    def set_num_180s(self, value):
        self.number_of_180s = value




    def increment_matches_won(self):
        self.matches_won += 1

    def get_matches_won(self):
        return self.matches_won

    def get_legs_won(self):
        return self.legs_won

    def set_legs_won(self, value):
        self.legs_won = value

    def increment_legs_won(self):
        self.legs_won += 1


    def set_starting_score(self, starting_score):
        self.current_score = starting_score

    def set_turn_count(self, value):
        self.turn_count = value
    def get_turn_count(self):
        return self.turn_count
    def increment_turn_count(self):
        self.turn_count += 1

    def decrement_turn_count(self):
        self.turn_count -= 1


    def set_won_leg(self, value):
        self.won_leg = value
    def get_won_leg(self):
        return self.won_leg

    def add_turn_score(self, score):
        self.turn_score_list.append(score)
        print(self.turn_score_list)
    def update_specific_dart_throw(self, dart_number):
        if(dart_number == 8):
            second_last_id = dart_throw_history_repo.get_second_last_throw_id()
            dart_throw_history_repo.update_throw_by_throw_id(second_last_id, score=0, is_knock_out=True)
        elif(dart_number == 9):
            last_id = dart_throw_history_repo.get_last_throw_id()
            dart_throw_history_repo.update_throw_by_throw_id(last_id, score=0, is_knock_out=True)
        else:
            pass




    def update_score(self, is_player_one, multiplier, value, is_bounce_out, is_foul_out, is_knock_out):
        #not using is_player_one anymore due to db changes but leaving as to not have to change usages (there are a lot)
        is_player_one = None
        score = multiplier * value

        self.current_score -= score

        player_id = player_repo.get_player_id_by_name(self.get_first_name(), self.get_last_name())



        if self.current_score <= 1 and self.current_score != 0:
            self.current_score += score
            dart_throw_history_repo.add_throw(player_id, self.current_score, self.multiplier, self.value, is_bounce_out,
                                              is_knock_out, is_foul_out)
            return False

        self.multiplier = multiplier
        self.value = value

        if self.current_score == 0:
            if multiplier == 2:
                self.won_leg = True
            else:
                self.current_score += score

        dart_throw_history_repo.add_throw(player_id, score, multiplier, value, is_bounce_out, is_knock_out, is_foul_out)
        print("-------------------- dart throw history --------------------")

        throws = dart_throw_history_repo.get_all_throws_for_player(player_id)
        for t in throws:
            print(t)
        print("------------------------------------------------------------")
        return True

    def get_dart_throws(self):
        return self.processed_throws

    def clear_dart_throws(self):
        self.processed_throws = []
        dart_throw_history_repo.delete_all_throws()

    def update_dart_throws(self):
        player_id = player_repo.get_player_id_by_name(self.get_first_name(), self.get_last_name())

        throws = dart_throw_history_repo.get_last_ten_throws_for_player(player_id)

        self.processed_throws = []



        for throw in throws:
            score, is_bounce_out, is_knock_out, is_foul_out = throw

            if is_bounce_out:
                self.processed_throws.append("IsBounceOut")
            elif is_knock_out:
                self.processed_throws.append("IsKnockOut")
            elif is_foul_out:
                self.processed_throws.append("IsFoulOut")
            else:
                self.processed_throws.append(str(score))






    def get_score(self):
        print("score in the player class: " + str(self.current_score))
        return self.current_score

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def set_first_name(self, first_name):
        self.old_first_name = self.first_name
        self.first_name = first_name

    def set_last_name(self, last_name):
        self.old_last_name = self.last_name
        self.last_name = last_name

    def add_player(self):
        player_repo.add_player(first_name=self.first_name, last_name=self.last_name)

    def set_winning_combination(self, winning_combination):
        self.winning_combination = ''.join(map(str, winning_combination))

    def get_winning_combination(self):
        return self.winning_combination

    def clear_winning_combinations(self):
        self.winning_combination = []



    def update_player_name(self):
        player_id = player_repo.get_player_id_by_name(self.get_first_name(), self.get_last_name())
        updated_attributes = {
            'first_name': self.first_name,
            'last_name': self.last_name
        }

        player_repo.update_player(player_id, **updated_attributes)


    def get_average_score_for_season(self):
        player_id = player_repo.get_player_id_by_name(self.get_first_name(), self.get_last_name())
        return matches_repo.get_average_turn_score_in_season(player_id)

    def get_number_of_180s_for_season(self):
        player_id = player_repo.get_player_id_by_name(self.get_first_name(), self.get_last_name())
        return matches_repo.get_total_180s_in_season(player_id)

    def get_current_rank_for_season(self):
        player_id = player_repo.get_player_id_by_name(self.get_first_name(), self.get_last_name())
        return matches_repo.get_player_rank(player_id)

    def get_last_win_for_season(self):
        player_id = player_repo.get_player_id_by_name(self.get_first_name(), self.get_last_name())
        return matches_repo.get_last_win_date(player_id)


from model import tournament_model
from model import player_model
from controller import main_controller
from controller import player_controller
from datetime import date
from view import view


class TournamentController(object):
    @classmethod
    def check_tournament_info(cls, input_text_value):
        while True:
            count = 0
            input_value = input('Tournament ' + input_text_value + ': ')
            # Checking if input value is a string (str)
            if type(input_value) is str:
                # Checking if input value is longer than 2
                if len(input_value) != 0 and len(input_value) >= 2:
                    # Looping through every character of the input value to check if theres digit in
                    for letter in input_value:
                        if letter.isdigit():
                            count += 1
                        else:
                            pass
                else:
                    print('Error, must be longer.')
                    continue
            else:
                print('Error, must be string text.')
                continue
            if count >= 1:
                print('Error, no numbers allowed.')
                continue
            else:
                return input_value

    @classmethod
    def set_tournament_rounds(cls):
        while True:
            tournament_rounds = int(input('How many rounds do you want : '))
            if type(tournament_rounds) is int:
                if tournament_rounds < 0:
                    print("Numbers of tours must be positive, " + str(tournament_rounds) + " given.")
                    continue
                if tournament_rounds == 0 or tournament_rounds is None:
                    tournament_rounds = 4
                    return tournament_rounds
                else:
                    return tournament_rounds
            else:
                print('Error, please enter a number not text.')
                continue

    @classmethod
    def set_time_control(cls):
        while True:
            time_control_input = input('The time control is: A) Bullet. B) Blitz. C) Coup rapide. [A/B/C]? : ')
            if time_control_input.lower() == 'a':
                time_control_input = "Bullet"
                print("Time control: {}.".format(time_control_input))
                return time_control_input
            elif time_control_input.lower() == 'b':
                time_control_input = "Blitz"
                print("Time control: {}.".format(time_control_input))
                return time_control_input
            elif time_control_input.lower() == 'c':
                time_control_input = "Coup rapide"
                print("Time control: {}.".format(time_control_input))
                return time_control_input
            else:
                print("Error, pick the value showed on screen.")
                continue

    @staticmethod
    def creating_pairs(players_list, rounds_count):

        if rounds_count == 1:
            # Getting all players in list and sorting them by their ladder ASC
            players_list.sort(key=lambda e: e['ladder'])

            # Making pairs with the Swiss rules
            middle = len(players_list)//2

            superior_players = players_list[:middle]
            inferior_players = players_list[middle:]

            pairs = zip(superior_players, inferior_players)

            return pairs
        else:
            players_list.sort(key=lambda x: x[2])
            print(players_list)


    @staticmethod
    def starting_match(pair):
        player1 = pair[0]
        player2 = pair[1]
        view.View.show_match_versus(player1, player2)
        result_match_input = input('Who won this match ?')

        return result_match_input

    @staticmethod
    def distributing_points(pair):

    @classmethod
    def start_tournament(cls, players_list, nb_rounds):
        rounds_count = 1
        list_of_match = []
        pair_list_of_match = []

        # Match[match1[([J1]vs[J2])([J1]vs[J2])([J1]vs[J2])], match2[([J1]vs[J2])([J1]vs[J2])([J1]vs[J2])]]
        while rounds_count < nb_rounds:
            list_of_current_round = []
            print('ROUND ' + str(rounds_count))
            if rounds_count == 1:
                pair_selector = cls.creating_pairs(players_list, rounds_count)
                for pair in pair_selector:
                    result_match_input = cls.starting_match(pair)
                    # If player 1 win the match
                    if result_match_input == '1':
                        player1['points'] = player1['points'] + 1
                        player2['points'] = player2['points'] + 0

                        player1_result = [player1['firstname'], player1['lastname'], player1['points']]
                        player2_result = [player2['firstname'], player2['lastname'], player2['points']]
                        pair_list_of_match.append(player1_result)
                        pair_list_of_match.append(player2_result)
                        match_result = (player1_result, player2_result)
                        list_of_current_round.insert(0, match_result)

                    # If player 2 win the match
                    elif result_match_input == '2':
                        print(player2['firstname'] + ' ' + player2['lastname'] + ' WON the match, +1pts')
                        player1['points'] = player1['points'] + 0
                        player2['points'] = player2['points'] + 1

                        player1_result = [player1['firstname'], player1['lastname'], player1['points']]
                        player2_result = [player2['firstname'], player2['lastname'], player2['points']]
                        pair_list_of_match.append(player1_result)
                        pair_list_of_match.append(player2_result)
                        match_result = (player1_result, player2_result)
                        list_of_current_round.insert(0, match_result)

                    else:
                        print('Match is even, the two players get +0.5pts')
                        player1['points'] = player1['points'] + 0.5
                        player2['points'] = player2['points'] + 0.5

                        player1_result = [player1['firstname'], player1['lastname'], player1['points']]
                        player2_result = [player2['firstname'], player2['lastname'], player2['points']]
                        pair_list_of_match.append(player1_result)
                        pair_list_of_match.append(player2_result)
                        match_result = (player1_result, player2_result)
                        list_of_current_round.insert(0, match_result)
                list_of_match.append(list_of_current_round)
                rounds_count += 1
            elif rounds_count != 1:
                cls.creating_pairs(pair_list_of_match, rounds_count)
                rounds_count += 1
            else:
                print('error')

    @classmethod
    def attribute_points_match(cls, match_result):
        if match_result == '1':
            print('1')
        elif match_result == '2':
            print('2')
        else:
            print('0.5')

    @classmethod
    def check_duplicate(cls, variable):
        for number in variable:
            if variable.count(number) > 1:
                return True
        return False

    @staticmethod
    def is_number(variable):
        # Check if only digit in array
        string = ""
        for number in variable:
            string += number
        result = string.isdigit()
        return result

    @classmethod
    def checking_validity_array(cls, array):
        # checking if only numeric values in array
        is_number = cls.is_number(array)
        if is_number:
            # checking if theres no duplicate in array
            check_duplicate = cls.check_duplicate(array)
            if check_duplicate:
                print('There\s duplicate value in your selection, re-do it')
                return False
            else:
                print('There\'s no duplicate in the selection')
                return True
        else:
            print('Only numbers allowed in the selection')
            return False

    @classmethod
    def select_players(cls):
        count = 0
        players_db_size = player_model.PlayerModel.get_player_db_size()

        # Display all players(names and ranks) from database
        while count < players_db_size:
            count += 1
            players = player_model.PlayerModel.get_players_by_id(count)
            view.View.display_all_players(count, players)

        # Selecting which player we want in input
        if count == players_db_size:

            # CONDITION POUR CHIFFRE > players_db_size ex: pas de 44 si db = 8
            count = 0
            while True:
                list_of_ids = []
                selected_players_input = input('Select players that will play the for the tournament: ').lstrip()
                # we push the Ids selected before in an array for query by id after
                for id_player in selected_players_input.split(","):
                    list_of_ids.append(id_player)
                result = cls.checking_validity_array(list_of_ids)
                if result:
                    break
                else:
                    continue

            # get players by id and return them in list
            list_of_players = player_model.PlayerModel.select_players_in_db(list_of_ids)
            print(list_of_players)

            while len(list_of_players) < 8:
                print(str(len(list_of_players)) + '/8 players')
                print('We\'re missing ' + str(int(8) - int(len(list_of_players))) + ' players')
                adding_players_input = input('Do you wanna add more players [M]anually or from the [L]ist ?')
                if adding_players_input.lower() == 'm':
                    added_player = player_controller.PlayerController.insert_new_player()
                    list_of_players.append(added_player)
                    print('We\'re missing ' + str(int(8) - int(len(list_of_players))) + ' players')
                elif adding_players_input.lower() == 'l':
                    print('list')
                    # RE AFFICHER LA LISTE DES JOUEURS MAIS NE PAS AFFICHER CEUX DEJA SELECTIONES
                    # RE CHOISIR EN LIMITANT AU NB DE PERSONNES MANQUANTES
            if len(list_of_players) == 8:
                print('We got the maximum players required! we good to go')
                return list_of_players

    @classmethod
    def insert_new_tournament(cls):
        #t_name = cls.check_tournament_info("Name")
        #t_place = cls.check_tournament_info("Place")
        t_date = str(date.today())
        #t_rounds = cls.set_tournament_rounds()
        t_turns = []
        t_players_list = cls.select_players()
        t_time_control = cls.set_time_control()
        #t_description = str(input('Choose the description for your tournament: '))

        # INSERTING INPUT DATA IN TOURNAMENT DB #
        new_tournament = tournament_model.TournamentModel(name='t_name', place='t_place', date=t_date, rounds=4, turns=t_turns, playerslist=t_players_list, timecontrol=t_time_control, description='t_description')

        serialized_tournament = {
            'name': new_tournament.name,
            'place': new_tournament.place,
            'date': new_tournament.date,
            'rounds': new_tournament.rounds,
            'turns': new_tournament.turns,
            'playerList': new_tournament.playerslist,
            'timeControl': new_tournament.timecontrol,
            'description': new_tournament.description
        }

        # INSERTING DATA IN TOURNAMENTS TABLE #
        insert_query = tournament_model.TournamentModel.insert_new_tournament(serialized_tournament)

        try:
            view.View.show_new_tournament_created(insert_query)
            start_tournament = input('Do you wanna start tournament now ? [Y/n]')
            if start_tournament.lower() == 'y':
                # DEBUT DU TOURNOI
                list_of_players = new_tournament.playerslist
                nb_rounds = new_tournament.rounds
                cls.start_tournament(list_of_players, nb_rounds)
            elif start_tournament.lower() == 'n':
                main_controller.start()
        except ValueError:
            print(ValueError)

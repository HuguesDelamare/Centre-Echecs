from model import tournament_model, player_model
from controller import main_controller, player_controller
from datetime import date
from time import strftime, localtime
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
    def creating_pairs(players_list, rounds_count, list=None):
        list_of_previous_match = list
        if rounds_count == 0:
            # Getting all players in list and sorting them by their ladder ASC
            players_list.sort(key=lambda e: e['ladder'])

            # Making pairs with the Swiss rules
            middle = len(players_list)//2

            superior_players = players_list[:middle]
            inferior_players = players_list[middle:]

            pairs = zip(superior_players, inferior_players)

            return pairs

        else:
            new_pair = []
            count_pair = 0
            i = 0
            y = 1

            # Sorting players by their total points
            players_list.sort(key=lambda x: x['points'])

            while count_pair < 4:
                match_tuple = (players_list[i], players_list[y])
                # Checking if players fought each others before

                # If the match between players already exist we look the next player
                if match_tuple in list:
                    y += 1
                    continue

                # If the match doesn't exist we push the pair in the array
                else:
                    new_pair.append(match_tuple)
                    i += 2
                    y += 2
                    count_pair += 1
                    continue

            return new_pair

    @staticmethod
    def starting_match(pair):
        # View that show player1 Vs player2
        view.View.show_match_versus(pair[0], pair[1])
        result_match_input = input('Who is the winner of this match? : ')

        return result_match_input

    @staticmethod
    def check_if_tournament_exist(tournament_name):
        print('hello')
        tournament_model.TournamentModel.check_if_tournament_exist(tournament_name)

    @staticmethod
    def distributing_points(winner, pair, playerlist):
        player1 = pair[0]
        player2 = pair[1]
        player_result_list = []

        if winner == '1':
            for i in range(len(playerlist)):
                if playerlist[i] == player1:
                    playerlist[i]['points'] += 1
                    player1_result = [player1['firstname'], player1['lastname'], player1['ladder'], player1['points']]
                    player2_result = [player2['firstname'], player2['lastname'], player2['ladder'], player2['points']]
                    match_tuple = (player1_result, player2_result)
                    return [match_tuple, playerlist]

        if winner == '2':
            for i in range(len(playerlist)):
                if playerlist[i] == player2:
                    playerlist[i]['points'] += 1
                    player1_result = [player1['firstname'], player1['lastname'], player1['ladder'], player1['points']]
                    player2_result = [player2['firstname'], player2['lastname'], player2['ladder'], player2['points']]
                    match_tuple = (player1_result, player2_result)
                    return [match_tuple, playerlist]
        else:
            for i in range(len(playerlist)):
                if playerlist[i] == player1:
                    playerlist[i]['points'] += 0.5
                    player1_result = [player1['firstname'], player1['lastname'], player1['ladder'], player1['points']]
                    player_result_list.append(player1_result)

            for i in range(len(playerlist)):
                if playerlist[i] == player2:
                    playerlist[i]['points'] += 0.5
                    player2_result = [player2['firstname'], player2['lastname'], player2['ladder'], player2['points']]
                    player_result_list.append(player2_result)

            match_tuple = tuple(player_result_list)
            return [match_tuple, playerlist]

    @classmethod
    def insert_new_round_db(cls, round, tournament_name):
        starting_datetime = strftime("%d-%m-%Y %H:%M", localtime())
        serialized_round = {
            'Round' + str(round): [],
            'StartingDatetime': starting_datetime,
            'FinishingDatetime': None
        }
        tournament_model.TournamentModel.insert_new_round(tournament_name, serialized_round)

    @classmethod
    def insert_new_match_db(cls, match, round_number, match_number, tournament_name):
        tournament_model.TournamentModel.insert_new_match(tournament_name, match, round_number)

    @classmethod
    def start_tournament(cls, players_list, nb_rounds, tournament_name):
        print(tournament_name)
        players_list = players_list
        rounds_count = 0
        list_of_match = []
        # turns : [Round1: [(player1 vs player2), (player2 vs player3], debut, fin, Round2: [(player1 vs player2), (player2 vs player3], debut, fin]
        while rounds_count < nb_rounds:
            list_of_current_round = []
            print('ROUND ' + str(rounds_count+1))
            cls.insert_new_round_db(rounds_count+1, tournament_name)
            if rounds_count == 0:
                pair_selector = cls.creating_pairs(players_list, rounds_count)
                match_count = 0
                for pair in pair_selector:
                    # Displaying players and admin has to pick a winner
                    result_match_input = cls.starting_match(pair)
                    match_count += 1
                    # Attributing points to players and displaying results
                    match_result = cls.distributing_points(result_match_input, pair, players_list)
                    list_of_current_round.insert(0, match_result[0])
                    cls.insert_new_match_db(match_result[0], rounds_count+1, match_count, tournament_name)
                    players_list = match_result[1]
                list_of_match.append(list_of_current_round)
                rounds_count += 1
            elif rounds_count >= 1:
                new_pair = cls.creating_pairs(players_list, rounds_count, list_of_match)
                match_count = 0
                for pair in new_pair:
                    result_match_input = cls.starting_match(pair)
                    match_count += 1
                    match_result = cls.distributing_points(result_match_input, pair, players_list)
                    list_of_current_round.insert(0, match_result[0])
                    cls.insert_new_match_db(match_result[0], rounds_count+1, match_count, tournament_name)
                    players_list = match_result[1]
                list_of_match.append(list_of_current_round)
                rounds_count += 1
            else:
                print('error')

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

    @staticmethod
    def id_player_exist(array, players_db_size):
        bool = ""
        for player_id in array:
            if int(players_db_size) >= int(player_id) > 0:
                bool = True
            else:
                bool = False
        return bool

    @classmethod
    def checking_validity_array(cls, array, players_db_size):
        # checking if only numeric values in array
        is_number = cls.is_number(array)
        if is_number:
            # checking if theres no duplicate in array
            check_duplicate = cls.check_duplicate(array)
            if check_duplicate:
                print('ERROR, there\'s duplicate players in your selection')
                return False
            else:
                check_id_player_exist = cls.id_player_exist(array, players_db_size)
                if check_id_player_exist:
                    return True
                else:
                    print('ERROR, player\'s ID doesn\'t exist')
                    return False
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

        # Selecting our players in input
        if count == players_db_size:
            count = 0
            while True:
                list_of_ids = []
                selected_players_input = input('Select players that will play the for the tournament: ').lstrip()
                # we push the Ids selected before in an array for query by id after
                for id_player in selected_players_input.split(","):
                    list_of_ids.append(id_player)
                result = cls.checking_validity_array(list_of_ids, players_db_size)
                if result:
                    break
                else:
                    continue

            # Get players by id and return them in list
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
        t_name = cls.check_tournament_info("Name")
        t_place = cls.check_tournament_info("Place")
        t_date = str(date.today())
        # t_rounds = cls.set_tournament_rounds()
        t_turns = []
        t_players_list = cls.select_players()
        t_time_control = cls.set_time_control()
        #t_description = str(input('Choose the description for your tournament: '))

        # INSERTING INPUT DATA IN TOURNAMENT DB #
        new_tournament = tournament_model.TournamentModel(name=t_name, place=t_place, date=t_date, rounds=4, turns=t_turns, playerslist=t_players_list, timecontrol=t_time_control, description='t_description')

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
            while True:
                start_tournament = input('Do you wanna start tournament now ? [Y/n]')
                if start_tournament.lower() == 'y':
                    list_of_players = new_tournament.playerslist
                    nb_rounds = new_tournament.rounds
                    print(new_tournament.name)
                    cls.start_tournament(list_of_players, nb_rounds, new_tournament.name)
                elif start_tournament.lower() == 'n':
                    main_controller.start()
                else:
                    print('ERROR : Asking if [Y]es or [N]o, ' + start_tournament + ' given.')
                    continue
        except ValueError:
            print(ValueError)

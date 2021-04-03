from datetime import date
from tinydb import TinyDB
import random


class Tournament(object):
    def __init__(self, name=None, place=None, date=None, rounds=None, turns=None, playerslist=None, timecontrol=None, description=None):
        self.name = str(name)
        self.place = str(place)
        self.date = str(date)
        self.rounds = int(rounds)
        self.turns = str(turns)
        self.playerslist = playerslist
        self.timecontrol = str(timecontrol)
        self.description = str(description)

    def __str__(self):
        return "New tournament created: " + str(self.__dict__)

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
            if time_control_input == "A" or time_control_input == "a":
                time_control_input = "Bullet"
                print("Time control: {}.".format(time_control_input))
                return time_control_input
            elif time_control_input == "B" or time_control_input == "b":
                time_control_input = "Blitz"
                print("Time control: {}.".format(time_control_input))
                return time_control_input
            elif time_control_input == "C" or time_control_input == "c":
                time_control_input = "Coup rapide"
                print("Time control: {}.".format(time_control_input))
                return time_control_input
            else:
                print("Error, pick the value showed on screen.")
                continue

    @classmethod
    def select_players(cls, players_picked):
        picked_players_list = []
        existing_id = []
        count = 0
        player_db = TinyDB('../Database/chessCenterDatabase.json').table('playerTable')
        players_db_size = len(player_db)

        if players_db_size < 8:
            print('Theres not enough players registred for the tournament.')
            return
        else:
            while count < players_picked:
                random_id = random.randint(1, players_db_size)
                selected_player = player_db.get(doc_id=random_id)
                if random_id in existing_id:
                    pass
                else:
                    picked_players_list.append(selected_player)
                    existing_id.append(random_id)
                    count += 1
        return picked_players_list

    @classmethod
    def creating_pairs(cls, players_list):
        # Getting all players in list and sorting them by their ladder ASC
        players_list.sort(key=lambda e: e['ladder'])

        # Making pairs with the Swiss rules
        middle = len(players_list)//2

        superior_players = players_list[:middle]
        inferior_players = players_list[middle:]

        pairs = zip(superior_players, inferior_players)
        # dict(zip(superiorPlayers, inferiorPlayers))

        cls.tournament_rounds(pairs)

    @classmethod
    def tournament_rounds(cls, pairs):
        print('Starting tournament')
        print('ROUND 1')
        for pair in pairs:
            print(pair)
        # Demander qui a gagner pour chaque pair
            # Désigner gagnant de round
            # Attribuer points par gagnants
        # Passer au round suivant

    @classmethod
    def insert_new_tournament(cls):
        t_name = cls.check_tournament_info("Name")
        t_place = cls.check_tournament_info("Place")
        t_date = str(date.today())
        t_rounds = cls.set_tournament_rounds()
        t_turns = []
        t_players_list = cls.select_players(8)
        t_time_control = cls.set_time_control()
        t_description = str(input('Choose the description for your tournament: '))

        # INSERTING INPUT DATA IN TOURNAMENT DB #
        new_tournament = Tournament(name=t_name, place=t_place, date=t_date, rounds=t_rounds, turns=t_turns, playerslist=t_players_list, timecontrol=t_time_control, description=t_description)

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
        tournament_db = TinyDB('../Database/chessCenterDatabase.json').table('tournamentTable')
        tournament_db.insert(serialized_tournament)

        return new_tournament

        # CREATING PAIRS FOR THE NEW TOURNAMENT CREATED #
        # players_list = new_tournament.playerslist
        # cls.creating_pairs(players_list)
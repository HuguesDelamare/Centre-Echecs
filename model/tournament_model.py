from tinydb import TinyDB, Query
import random

# Global variables that represent the different DB used
player_db = TinyDB('./Database/chessCenterDatabase.json').table('playerTable')
tournament_db = TinyDB('./database/chessCenterDatabase.json').table('tournamentTable')


class TournamentModel(object):
    def __init__(self, name=None, place=None, date=None, rounds=None, turns=None, playerslist=None, timecontrol=None, description=None, ongoing=True):
        self.name = str(name)
        self.place = str(place)
        self.date = str(date)
        self.rounds = int(rounds)
        self.turns = list(turns)
        self.playerslist = list(playerslist)
        self.timecontrol = str(timecontrol)
        self.description = str(description)
        self.ongoing = bool(ongoing)

    @staticmethod
    def select_players(players_picked):
        picked_players_list = []
        existing_id = []
        count = 0
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

    # Inserting fresh created tournament to DB
    @staticmethod
    def insert_new_tournament(serialized_tournament):
        tournament_db.insert(serialized_tournament)
        return serialized_tournament

    # Function to insert a new round in the tournament rounds list
    @staticmethod
    def insert_new_round(tournament_name, serialized_round):
        get_tournament = tournament_db.search(Query().name == str(tournament_name))
        if len(get_tournament) != 0:
            tournament = get_tournament[0]
            tournament_turns = tournament['turns']
            tournament_turns.append(serialized_round)
            tournament['turns'] = tournament_turns
            tournament_db.remove(Query().name == str(tournament_name))
            result = tournament_db.insert(tournament)
            return result
        else:
            print('ERROR, no tournament found')

    # Function to insert a new match to the current round
    @staticmethod
    def insert_new_match(tournament_name, match, round_number):
        # Get the tournament data matching the tournament name
        get_tournament = tournament_db.search(Query().name == str(tournament_name))
        # If the tournament exist
        if len(get_tournament) != 0:
            tournament = get_tournament[0]
            tournament_round_index = int(round_number-1)
            tournament_round = tournament['turns'][tournament_round_index]['Round'+str(round_number)]
            tournament_round.append(match)
            tournament['turns'][tournament_round_index]['Round'+str(round_number)] = tournament_round
            tournament_db.remove(Query().name == str(tournament_name))
            result = tournament_db.insert(tournament)
            return result
        else:
            print('ERROR, no tournament found')

    # Updating the datetime of the end of the tournament
    @staticmethod
    def end_date_round(tournament_name, round_number, end_date):
        # Get the tournament data matching the tournament name
        get_tournament = tournament_db.search(Query().name == str(tournament_name))
        if len(get_tournament) != 0:
            tournament = get_tournament[0]
            tournament_round_index = int(round_number-1)
            tournament['turns'][tournament_round_index]['FinishingDatetime'] = end_date
            tournament_db.remove(Query().name == str(tournament_name))
            tournament_db.insert(tournament)

    # Tournament is done so we set it to 'done' by changing ongoing value to False
    @staticmethod
    def end_tournament(tournament_name):
        get_tournament = tournament_db.search(Query().name == str(tournament_name))
        if len(get_tournament) != 0:
            tournament = get_tournament[0]
            tournament['ongoing'] = False
            tournament_db.remove(Query().name == str(tournament_name))
            tournament_db.insert(tournament)
            return tournament['ongoing']

    # Function to check if a tournament is already ongoing
    @staticmethod
    def check_ongoing_tournament():
        result = tournament_db.search(Query().ongoing == True)
        if len(result) == 0:
            return False
        else:
            return True

from tinydb import TinyDB, Query
import random
import json

player_db = TinyDB('./Database/chessCenterDatabase.json').table('playerTable')
tournament_db = TinyDB('./database/chessCenterDatabase.json').table('tournamentTable')


class TournamentModel(object):
    def __init__(self, name=None, place=None, date=None, rounds=None, turns=None, playerslist=None, timecontrol=None, description=None):
        self.name = str(name)
        self.place = str(place)
        self.date = str(date)
        self.rounds = int(rounds)
        self.turns = list(turns)
        self.playerslist = list(playerslist)
        self.timecontrol = str(timecontrol)
        self.description = str(description)
        self.live = bool(True)

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

    @staticmethod
    def insert_new_tournament(serialized_tournament):
        tournament_db.insert(serialized_tournament)
        return serialized_tournament

    """@staticmethod
    def insert_new_round(tournament_name, serialized_round):
        print(serialized_round)
        get_tournament = tournament_db.search(Query().name == str(tournament_name))
        if len(get_tournament) != 0:
            print(get_tournament)
            tournament_round = get_tournament[0]
            print(tournament_round)
            tournament_round['turns'].append(serialized_round)
            print(tournament_round)
            try:
                print('insert')
                # tournament_db.remove(Query().name == str(tournament_name))
                # result = tournament_db.insert(tournament_round)
                result = tournament_db.update({'turns': tournament_round}), Query().name == str(tournament_name)
                return result

            except Exception as e:
                print(e)
        else:
            print('ERROR, no tournament found')"""

    @staticmethod
    def insert_new_round(tournament_name, serialized_round):
        # print(serialized_round)
        get_tournament = tournament_db.search(Query().name == str(tournament_name))
        if len(get_tournament) != 0:
            tournament = get_tournament[0]
            print(tournament)
            tournament_turns = tournament['turns']
            print(tournament_turns)
            tournament_turns.append(serialized_round)
            print(tournament_turns)
            tournament['turns'] = tournament_turns
            print(tournament)
            tournament_db.remove(Query().name == str(tournament_name))
            result = tournament_db.insert(tournament)
            return result
        else:
            print('ERROR, no tournament found')

    @staticmethod
    def insert_new_match(tournament_name, match, round_number, match_number):
        # Get the tournament data matching the name
        get_tournament = tournament_db.search(Query().name == str(tournament_name))
        # If the tournament exist
        if len(get_tournament) != 0:
            tournament = get_tournament[0]
            tournament_round = tournament['turns'][0]['Round'+str(round_number)]
            tournament_round.append(match)
            tournament['turns'][0]['Round'+str(round_number)] = tournament_round
            tournament_db.remove(Query().name == str(tournament_name))
            result = tournament_db.insert(tournament)
            return result
        else:
            print('ERROR, no tournament found')
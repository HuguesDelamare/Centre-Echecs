from tinydb import TinyDB, Query
from tinydb.operations import add
from tinydb import where
import random


class TournamentModel(object):
    def __init__(self, name=None, place=None, date=None, rounds=None, turns=None, playerslist=None, timecontrol=None, description=None):
        self.name = str(name)
        self.place = str(place)
        self.date = str(date)
        self.rounds = int(rounds)
        self.turns = str(turns)
        self.playerslist = list(playerslist)
        self.timecontrol = str(timecontrol)
        self.description = str(description)

    """def __str__(self):
        return "New tournament created: " + str(self.__dict__)"""

    @staticmethod
    def select_players(players_picked):
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

    @staticmethod
    def insert_new_tournament(serialized_tournament):
        tournament_db = TinyDB('../database/chessCenterDatabase.json').table('tournamentTable')
        tournament_db.insert(serialized_tournament)
        return serialized_tournament

    @staticmethod
    def insert_new_round(tournament_name, serialized_round):
        tournament_db = TinyDB('../database/chessCenterDatabase.json').table('tournamentTable')
        search_db = tournament_db.search(Query().name == str(tournament_name))
        if len(search_db) != 0:
            result = tournament_db.update({'turns': serialized_round}), Query().name == str(tournament_name)
            return result
        else:
            print('ERROR, no tournament found')

    @staticmethod
    def insert_new_match(tournament_name, match, round_number):
        # Database and table we're working on
        tournament_db = TinyDB('../database/chessCenterDatabase.json').table('tournamentTable')
        # Get the tournament data matching the name
        get_tournament = tournament_db.search(Query().name == str(tournament_name))
        # If the tournament exist
        if len(get_tournament) != 0:
            for tournament in get_tournament:
                print(tournament)
                for key in tournament:
                    if key == 'turns':
                        for x in tournament[key]:
                            key2 = x
                            value = tournament[key][key2]
                            if type(value) is list:
                                print('key : ' + key)
                                print('value : ' + key2)
                                # Updating the database by adding the new value
                                result = tournament_db.update(add(value, match), Query().name == str(tournament_name))
                                print(get_tournament)
                                return result
        else:
            print('ERROR, no tournament found')

    @staticmethod
    def check_if_tournament_exist(tournament_name):
        tournament_db = TinyDB('../database/chessCenterDatabase.json').table('tournamentTable')
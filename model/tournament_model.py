from tinydb import TinyDB, Query
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
    def insert_new_round():
        tournament_db = TinyDB('../database/chessCenterDatabase.json').table('tournamentTable')

        tournament_db.all()

        for i in tournament_db.all():
            print(i)

    @staticmethod
    def insert_new_match():
        print('match')

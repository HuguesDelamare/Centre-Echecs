from tinydb import TinyDB, Query

player_db = TinyDB('../database/chessCenterDatabase.json').table('playerTable')


class PlayerModel(object):
    def __init__(self, lastname=None, firstname=None, birthdate=None, gender=None, ladder=None, points=0):
        self.lastname = str(lastname)
        self.firstname = str(firstname)
        self.birthdate = str(birthdate)
        self.gender = str(gender)
        self.ladder = ladder
        self.points = float(points)

    """def __str__(self):
        return "New Player created : " + str(self.__dict__)"""

    @staticmethod
    def insert_new_player(serialized_player):
        global player_db
        player_db.insert(serialized_player)
        return serialized_player

    @staticmethod
    def get_players_by_id(player_id):
        global player_db
        result = player_db.get(doc_id=player_id)
        return result

    @staticmethod
    def select_players_in_db(list_id):
        list_of_players = []
        global player_db
        for player_id in list_id:
            player_id = int(player_id)
            result = player_db.get(doc_id=player_id)
            list_of_players.append(result)
        return list_of_players

    @staticmethod
    def get_player_db_size():
        player_db_size = len(player_db)
        return player_db_size

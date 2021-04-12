from tinydb import TinyDB, Query

player_db = TinyDB('../database/chessCenterDatabase.json').table('playerTable')

class PlayerModel(object):

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
    def get_all_players_in_db(list_id):
        list_of_players = []
        global player_db
        for player_id in list_id:
            player = player_db.get(doc_id=player_id)
            list_of_players.append(player)
        return list_of_players

    @staticmethod
    def get_player_db_size():
        player_db_size = len(player_db)
        return player_db_size

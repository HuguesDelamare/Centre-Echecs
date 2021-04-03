from model import player_model
from view import view


class PlayerController(object):

    @staticmethod
    def show_new_player(player):
        # display the new player
        view.View().show_new_player_created(player)

    @staticmethod
    def set_player():
        # set new player in DB
        player_data = player_model.Player().insert_new_player()
        # instantiate the view after inserting player
        PlayerController.show_new_player(player_data)



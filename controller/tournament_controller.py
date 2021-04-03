from model import tournament_model
from view import view


class TournamentController(object):

    @staticmethod
    def show_new_tournament(tournament):
        # display the new player
        view.View.show_new_tournament_created(tournament)

    @staticmethod
    def set_new_tournament():
        # set new tournament in DB
        tournament_data = tournament_model.Tournament.insert_new_tournament()
        # instantiate the view after inserting tournament
        TournamentController.show_new_tournament(tournament_data)





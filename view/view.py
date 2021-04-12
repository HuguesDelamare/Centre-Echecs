class View(object):

    @staticmethod
    def show_menu():
        print("1.Create player")
        print("2.Create tournament")
        print("3.Check ladder")
        print("4.Exit")

    @staticmethod
    def show_new_player_created(player):
        return print('New player ' + player['firstname'] + ' ' + player['lastname'] + ' registred.')

    @staticmethod
    def show_new_tournament_created(tournament):
        return print('New tournament ' + tournament['name'] + ' was created the ' + tournament['date'] + ' for a total of ' + str(tournament['rounds']) + ' rounds and ' + str(len(tournament['playerList'])) + ' players.')

    @staticmethod
    def exit_application():
        print('Quitting application!')

    @staticmethod
    def display_all_players(count, player):
        print("Player n°" + str(count) + ' : ' + player['firstname'] + ' ' + player['lastname'] + ", Rank : " + str(player['ladder']))


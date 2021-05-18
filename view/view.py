class View(object):

    @staticmethod
    def show_menu():
        print("1. Create player")
        print("2. Create tournament")
        print("3. Check reports")
        print("4. Exit")

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
        print(str(count) + ': ' + player['firstname'] + ' ' + player['lastname'] + " |" + " Rank: " + str(player['ladder']))

    @staticmethod
    def show_match_versus(player1, player2):
        print(player1['firstname'] + ' ' + player1['lastname'] + ' VS ' + player2['firstname'] + ' ' + player2['lastname'])

    @staticmethod
    def display_unique_match_result(player):
        print(player['firstname'] + ' ' + player['lastname'] + ' WON the match, +1pts')

    @staticmethod
    def end_tournament_message():
        print('Tournament is over !')

    @staticmethod
    def show_ladder_menu():
        print("1. Players ladder")
        print("2. Tournaments ladder")
        print("3. Back to menu")

    @staticmethod
    def ongoing_tournament_menu():
        print('A tournament is already ongoing, need to be done before making a new one.')
        print("1. Continue the ongoing tournament")
        print("2. Back to menu")
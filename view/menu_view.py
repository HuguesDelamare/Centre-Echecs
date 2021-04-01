from controller import player_controller
from controller import tournament_controller

class View(object):
    def show_starting_menu(self):
        while True:
            try:
                answer = int(input('What do you wanna do ? : '))
                if answer == 1:
                    create_player = player_controller
                elif answer == 2:
                    print('2')
                elif answer == 3:
                    print('3')
                elif answer == 4:
                    print('4')
                else:
                    continue
            except ValueError:
                print('Error, enter a good value.')
                continue

    def show_menu(self):
        print("1.Create player")
        print("2.Create tournament")
        print("3.Check ladder")
        print("4.Exit")

    def show_new_player_created(self, player):
        print(player)

    def show_new_tournament_created(self, tournament):
        print(tournament)

    def exit_application(self):
        print('Goodbye!')
from view import view
from controller import player_controller
from controller import tournament_controller


def start():
    while True:
        view.View().show_menu()
        try:
            answer = int(input('What do you wanna do ? : '))
            if answer == 1:
                player_controller.PlayerController().set_player()
            elif answer == 2:
                tournament_controller.TournamentController().set_new_tournament()
            elif answer == 3:
                print('3')
            elif answer == 4:
                view.View.exit_application()
                exit()
            else:
                continue
        except ValueError:
            print('Error, enter a good value.')
            continue

if __name__ == "__main__":
    start()
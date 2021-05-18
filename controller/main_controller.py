import controller
import view
import sys


def start():
    while True:
        view.View().show_menu()
        try:
            answer = int(input('> '))
            if answer == 1:
                controller.playercontroller.insert_new_player()
            elif answer == 2:
                check_ongoing_tournament = controller.tournamentcontroller.check_tournament_live()
                if check_ongoing_tournament:
                    view.View.ongoing_tournament_menu()
                    answer = int(input('> '))
                    if answer == 1:
                        print('continue the tournament')
                    else:
                        continue
                else:
                    controller.tournamentcontroller.insert_new_tournament()
            elif answer == 3:
                view.View.show_ladder_menu()
                while True:
                    answer = int(input('> '))
                    if answer == 1:
                        controller.playercontroller.get_all_players_in_db()
                    elif answer == 2:
                        print('checking tournament ladder')
                    elif answer == 3:
                        start()
                    else:
                        print('ERROR, wrong value given.')
            elif answer == 4:
                view.View.exit_application()
                sys.exit(0)
            else:
                continue
        except ValueError:
            print('ERROR, wrong value given.')
            continue

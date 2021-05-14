import controller
import view


def start():
    while True:
        view.View().show_menu()
        try:
            answer = int(input('What do you wanna do ? : '))
            if answer == 1:
                controller.playercontroller.insert_new_player()
            elif answer == 2:
                tournament_is_live = controller.tournamentcontroller.check_tournament_live()
                if tournament_is_live:
                    print('A tournament is already live, Do you wanna continue to this one ?')
                else:
                    controller.tournamentcontroller.insert_new_tournament()
            elif answer == 3:
                view.View.show_ladder_menu()
                while True:
                    answer = int(input('What do you wanna do ? : '))
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
                exit()
            else:
                continue
        except ValueError:
            print('ERROR, wrong value given.')
            continue

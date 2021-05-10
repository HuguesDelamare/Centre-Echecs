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
                controller.tournamentcontroller.insert_new_tournament()
            elif answer == 3:
                view.View.show_ladder_menu()
                while True:
                    answer = int(input('What do you wanna do ? : '))
                    if answer == 1:
                        print('checking player ladder')
                        controller.playercontroller.get_all_players_in_db()
                    elif answer == 2:
                        print('checking tournament ladder')
                    elif answer == 3:
                        print('return')
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


if __name__ == "__main__":
    start()

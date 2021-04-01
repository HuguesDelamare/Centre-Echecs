from model import player_model
from view import menu_view

def start():
    while True:
        menu_view.View().show_menu()
        try:
            answer = int(input('What do you wanna do ? : '))
            if answer == 1:
                print('1')
                player_model.Player().createPlayer()
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

if __name__ == "__main__":
    start()
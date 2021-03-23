from view import menu_view
from model import tournament_model
from model import tournament_player_model

def showPlayer():
    return menu_view.showNewPlayer(tournament_player_model.createPlayer())

def showTournament():
    return menu_view.shoNewTournament(tournament_model.createTournament())

def backToMenu():
    start()

### Menu where user can choose what to do ###
def start():
    menu_view.startView()
    while True:
        try:
            answer = int(input('What do you wanna do ? : '))
            if answer == 1:
                showPlayer()
                backToMenu()
            elif answer == 2:
                showTournament()
                backToMenu()
            elif answer == 3:
                print('Creating ladder')
            elif answer == 4:
                menu_view.endView()
            else:
                continue
        except ValueError:
            print('Error, enter a good value.')
            continue

if __name__ == "__main__":
   #running controller function
   start()
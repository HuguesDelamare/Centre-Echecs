from view import menu_view
from model import tournament_model
from model import tournament_player_model

def createPlayerMenu():
    return menu_view.showNewPlayer(tournament_player_model.createPlayer())

def createTournamentMenu():
    return menu_view.shoNewTournament(tournament_model.createTournament())

def returnMainMenu():
    start()

def exitMenu():
    return menu_view.endView()

### Menu where user can choose what to do ###
def start():
    menu_view.startView()
    while True:
        try:
            answer = int(input('What do you wanna do ? : '))
            if answer == 1:
                createPlayerMenu()
                returnMainMenu()
            elif answer == 2:
                createTournamentMenu()
                returnMainMenu()
            elif answer == 3:
                print('Creating ladder')
            elif answer == 4:
                exitMenu()
            else:
                continue
        except ValueError:
            print('Error, enter a good value.')
            continue

if __name__ == "__main__":
   #running controller function
   start()
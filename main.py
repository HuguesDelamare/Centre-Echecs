import random
from datetime import date
from tinydb import TinyDB, Query


def randomColor():
    colors = ['White', 'Black']
    print(random.choice(colors))

def makingPairs(selectedPlayers):
    Lst = [("Amanda", 35), ("John", 30), ("Monica", 25)]
    Lst.sort(key=lambda x: x[1])
    print(Lst)
    """for player in selectedPlayers:
        print(player['firstname'], ': Rang', player['ladder'])"""


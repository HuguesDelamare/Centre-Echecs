from datetime import date
from tinydb import TinyDB, Query
import random

class Tournament:
    def __init__(self, name, place, date, turns, tours, players, timecontrol, description):
        self.name = str(name)
        self.place = str(place)
        self.date = str(date)
        self.turns = int(turns)
        self.tours = str(tours)
        self.players = players
        self.timecontrol = str(timecontrol)
        self.description = str(description)

    def __str__(self):
        return "New tournament created: " + str(self.__dict__)

    @staticmethod
    def checkTournamentInfos(inputTextValue):
        while True:
            count = 0
            inputvalue = input('Tournament ' + inputTextValue + ': ')
            #Checking if input value is a string (str)
            if type(inputvalue) is str:
                #Checking if input value is longer than 2
                if len(inputvalue) != 0 and len(inputvalue) >= 2:
                    #Looping through every character of the input value to check if theres digit in
                    for letter in inputvalue:
                        if letter.isdigit():
                            count += 1
                        else:
                            pass
                else:
                    print('Error, must be longer.')
                    continue
            else:
                print('Error, must be string text.')
                continue
            #print("Total digit present : ", count)
            if count >= 1:
                print('Error, no numbers allowed.')
                continue
            else:
                return inputvalue

    @staticmethod
    def setTournamentTurns():
        while True:
            tournamentTurns = int(input('How many tours do you want : '))
            if type(tournamentTurns) is int:
                if tournamentTurns < 0:
                    print("Numbers of tours must be positive, " + str(tournamentTurns) + " given.")
                    continue
                if tournamentTurns == 0 or tournamentTurns is None:
                    tournamentTurns = 4
                    return tournamentTurns
                else:
                    return tournamentTurns
            else:
                print('Error, please enter a number not text.')
                continue

    @staticmethod
    def selectTimeControl():
        while True:
            inputValue = input('The time control is: A) Bullet. B) Blitz. C) Coup rapide. [A/B/C]? : ')
            if inputValue == "A" or inputValue == "a":
                inputValue = "Bullet"
                print("Time control: {}.".format(inputValue))
                return inputValue
            elif inputValue == "B" or inputValue == "b":
                inputValue = "Blitz"
                print("Time control: {}.".format(inputValue))
                return inputValue
            elif inputValue == "C" or inputValue == "c":
                inputValue = "Coup rapide"
                print("Time control: {}.".format(inputValue))
                return inputValue
            else:
                print("Error, pick the value showed on screen.")
                continue

    @staticmethod
    def pickPlayers(numberPlayersPicked):
        listPickedPlayers = []
        existingId = []
        count = 0
        playerDB = TinyDB('../Database/playersDB.json').table('playerTable')
        playersDBSize = len(playerDB)
        #print(playersDBSize)

        if playersDBSize < 8:
            print('Theres not enough players registred for the tournament.')
            return
        else:
            while count < numberPlayersPicked:
                randomId = random.randint(1, playersDBSize)
                pickedPlayer = playerDB.get(doc_id=randomId)
                if randomId in existingId:
                    pass
                else:
                    listPickedPlayers.append(pickedPlayer)
                    existingId.append(randomId)
                    count += 1
        return listPickedPlayers

    @staticmethod
    def creatingPairs(listofplayers):
        roundCount = 0
        #Getting all players in list and sorting them by their ladder ASC
        listofplayers.sort(key=lambda e: e['ladder'])
        #Making pairs with the Swiss rules

        middle = len(listofplayers)//2
        #print("Top ladder players: ")
        superiorPlayers = listofplayers[:middle]
        #print(superiorPlayers)

        #print("Lower ladder players: ")
        inferiorPlayers = listofplayers[middle:]
        #print(inferiorPlayers)

        pairs = zip(superiorPlayers, inferiorPlayers)
        #dict(zip(superiorPlayers, inferiorPlayers))

        tournamentRounds(pairs)

    @staticmethod
    def tournamentRounds(pairs):
        print('Starting tournament')
        print('ROUND 1')
        for pair in pairs:
            print(pair)
        #Demander qui a gagner pour chaque pair
            #Désigner gagnant de round
            #Attribuer points par gagnants
        #Passer au round suivant
        #

    @staticmethod
    def createTournament(self):
        tournamentName = self.checkTournamentInfos("Name")
        tournamentPlace = self.checkTournamentInfos("Place")
        tournamentDate = str(date.today())
        tournamentTurns = self.setTournamentTurns()
        tournamentTours = []
        tournamentPlayersList = self.pickPlayers(8)
        tournamentTimeControl = self.selectTimeControl()
        tournamentDescription = str(input('Choose the description for your tournament: '))

        ### INSERTING INPUT DATA IN TOURNAMENT DB ###
        newTournament = Tournament(name=tournamentName, place=tournamentPlace, date=tournamentDate, turns=tournamentTurns, tours=tournamentTours, players=tournamentPlayersList, timecontrol=tournamentTimeControl, description=tournamentDescription)

        serializedTournament = {
            'name': tournamentName,
            'place': tournamentPlace,
            'date': tournamentDate,
            'turns': tournamentTurns,
            'tours': tournamentTours,
            'playerList': tournamentPlayersList,
            'timeControl': tournamentTimeControl,
            'description': tournamentDescription
        }

        tournamentDB = TinyDB('../Database/chessCenterDatabase.json').table('tournamentTable')
        tournamentDB.insert(serializedTournament)

        ###  CREATING PAIRS FOR THE NEW TOURNAMENT CREATED ###
        listofplayers = newTournament.players
        creatingPairs(listofplayers)



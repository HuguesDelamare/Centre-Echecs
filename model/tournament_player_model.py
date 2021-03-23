import json
import random
import datetime
from tinydb import TinyDB, Query

class Player:
    def __init__(self, lastname, firstname, birthdate, gender, ladder):
        self.lastname = str(lastname)
        self.firstname = str(firstname)
        self.birthdate = str(birthdate)
        self.gender = str(gender)
        self.ladder = int(ladder)

    def __str__(self):
        return "New player created: " + str(self.__dict__)

# select 8 players from the DB for the new tournament
def pickPlayers(numberToPick):
    listPickedPlayers = []
    existingId = []
    count = 0
    playersDB = TinyDB('playersDB.json')
    playersDBSize = len(playersDB)
    while count < numberToPick:
        randomId = random.randint(1, playersDBSize)
        pickedPlayer = playersDB.get(doc_id=randomId)
        if randomId in existingId:
            pass
        else:
            listPickedPlayers.append(pickedPlayer)
            existingId.append(randomId)
            count += 1
    print(listPickedPlayers)
    print(existingId)

def setPlayerBirthdate():
    formatList = ["%d-%m-%Y", "%d/%m/%Y", "%d %m %Y"]
    while True:
        playerBirthdate = str(input('Player birthdate: '))
        for format in formatList:
            try:
                date = datetime.datetime.strptime(playerBirthdate, format).date()
                return date
            except ValueError:
                pass

### FUNCTION TO PICK THE GENDER OF THE NEW PLAYER ###
def setPlayerGender():
    while True:
        playerGender = input('Player gender: [M]ale or [F]emale ?: ')
        if playerGender == "M" or playerGender == "F":
            return playerGender
        else:
            continue

###  FUNCTION TO CHECK IF DATA INPUT ARE VALID ###
def checkPlayerInfos(inputTextValue):
    while True:
        count = 0
        inputvalue = input('Player ' + inputTextValue + ': ')
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

def createPlayer():
    playerFirstname = checkPlayerInfos("Firstname")
    playerLastname = checkPlayerInfos("Lastname")
    playerBirthdate = setPlayerBirthdate()
    playerGender = setPlayerGender()

    ### INSERTING INPUT DATA IN PLAYER DB ###
    newPlayer = Player(lastname=playerLastname, firstname=playerFirstname, birthdate=playerBirthdate, gender=playerGender, ladder=0)

    serializedPlayer = {
        'lastname': newPlayer.lastname,
        'firstname': newPlayer.firstname,
        'birthdate': newPlayer.birthdate,
        'gender': newPlayer.gender,
        'ladder': newPlayer.ladder
    }

    ### INSERTING INPUT DATA IN PlAYER DB ###
    playerDB = TinyDB('../Database/playersDB.json')
    table = playerDB.table('playerTable')
    table.insert(serializedPlayer)

    return newPlayer

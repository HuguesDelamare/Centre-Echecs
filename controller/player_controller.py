import json
import random
import datetime
from model import player_model
from tinydb import TinyDB, Query

class player_Controller(object):

    def __init__(self, model, view):
        self.model = model
        self.view = view

    @classmethod
    def setPlayerBirthdate(self):
        formatList = ["%d-%m-%Y", "%d/%m/%Y", "%d %m %Y"]
        while True:
            playerBirthdate = str(input('Player Birthdate: '))
            for format in formatList:
                try:
                    date = datetime.datetime.strptime(playerBirthdate, format).date()
                    return date
                except ValueError:
                    pass

    ### FUNCTION TO PICK THE GENDER OF THE NEW PLAYER ###
    @classmethod
    def setPlayerGender(self):
        while True:
            playerGender = input('Player gender: [M]ale or [F]emale ?: ')
            if playerGender == "M" or playerGender == "F":
                return playerGender
            else:
                continue

    ###  FUNCTION TO CHECK IF DATA INPUT ARE VALID ###
    @classmethod
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

    @classmethod
    def createPlayer(self):
        playerFirstname = self.checkPlayerInfos("Firstname")
        playerLastname = self.checkPlayerInfos("Lastname")
        playerBirthdate = self.setPlayerBirthdate()
        playerGender = self.setPlayerGender()

        ### INSERTING INPUT DATA IN PLAYER DB ###
        newPlayer = self.Player(lastname=playerLastname, firstname=playerFirstname, birthdate=playerBirthdate, gender=playerGender, ladder=0)

        serializedPlayer = {
            'lastname': newPlayer.lastname,
            'firstname': newPlayer.firstname,
            'birthdate': newPlayer.birthdate,
            'gender': newPlayer.gender,
            'ladder': newPlayer.ladder
        }

        ### INSERTING INPUT DATA IN PlAYER DB ###
        playerDB = TinyDB('../Database/chessCenterDatabase.json')
        table = playerDB.table('playerTable')
        table.insert(serializedPlayer)

        return newPlayer

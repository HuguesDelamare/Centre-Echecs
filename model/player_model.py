from controller import player_controller

class Player(object):
    def __init__(self, lastname, firstname, birthdate, gender, ladder):
        self.lastname = str(lastname)
        self.firstname = str(firstname)
        self.birthdate = str(birthdate)
        self.gender = str(gender)
        self.ladder = int(ladder)

    def __str__(self):
        return "New player created: " + str(self.__dict__)

    def createPlayer(self):
        return player_controller.createPlayer()

    def checkPlayerInfos(self):
        return player_controller.checkPlayerInfos()

    def setPlayerGender(self):
        return player_controller.setPlayerGender()

    def setPlayerBirthdate(self):
        return player_controller.setPlayerBirthdate()


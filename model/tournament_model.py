from controller import tournament_controller

class Tournament(object):
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

    def createTournament(self):
        tournament_controller.createTournament()

    def checkTournamentInfos(self):
        return tournament_controller.checkTournamentInfos()

    def setTournamentTurns(self):
        return tournament_controller.setTournamentTurns()

    def selectTimeControl(self):
        return tournament_controller.selectTimeControl()

    def pickPlayers(self):
        return tournament_controller.pickPlayers()

    def tournamentRounds(self, pairs):
        return tournament_controller.tournamentRounds(pairs)

    def creatingPairs(self):
        return tournament_controller.creatingPairs()

from Player import Team
from Deck import Deck


class Table:
    """ This class is responsible for the Table management"""

    def __init__(self):
        self.freeSpots = 4
        self.teamA = Team()
        self.teamB = Team()

    def getPoints(self, team):
        if(team == 'A'):
            return self.teamA.getPoints()
        elif(team == 'B'):
            return self.teamB.getPoints()
        else:
            return ('ERROR-> No team called' + str(team))

    def sitPlayer(self, p):
        if(self.freeSpots % 2 == 0 and self.freeSpots > 0):
            self.teamA.addPlayer(p)
            self.freeSpots = self.freeSpots - 1
        elif(self.freeSpots % 2 == 1):
            self.teamB.addPlayer(p)
            self.freeSpots = self.freeSpots - 1
        else:
            print("Table is full.")

    def regenSpot(self):
        pass  # if player exits server, it should create an event that regenerates that free spot and team position

class Card:
    """ This class is for each individual card."""

    def __init__(self, suit, value, buffer):
        self.suit = suit
        self._value = value
        self.points = self.getPoints(buffer)
        self.name = self.getName(buffer)

    def getName(self, buffer):
        if self._value < 10:
            return str(self._value)
        elif self._value == 2+buffer:
            return "Queen"
        elif self._value == 3+buffer:
            return "Jack"
        elif self._value == 4+buffer:
            return "King"
        elif self._value == 10+buffer:
            return str(7)
        elif self._value == 11+buffer:
            return "Ace"

    def getPoints(self, buffer):
        points = self._value-buffer
        if points < 0:
            return 0
        else:
            return points

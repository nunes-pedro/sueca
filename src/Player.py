#from collections import deque


class Player:
    """This class is responsible for player actions """

    def __init__(self, role, order):
        self.role = role
        self.tableSpot = order
        self.hand = []

    def getHand(self, deck):
        for i in range(10):
            self.hand.append(deck.cards.pop(0))

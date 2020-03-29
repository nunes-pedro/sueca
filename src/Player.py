#from collections import deque
from Card import Card  # decide if it remains here


class Player:
    """This class is responsible for player actions """

    def __init__(self):
        self.role = 'Not_Assigned'
        #self.tableSpot = order
        self.hand = []
        # TODO: message for new user and request input
        self.uid = ' '

    def getHand(self, deck):
        for i in range(10):
            self.hand.append(deck.cards.pop(0))

    def assignRole(self, role):
        self.role = role

    def doJob(self, deck):
        if(self.role == 'shuffler'):
            # TODO: message for shuffler
            print("How many times do you want the cards to be shuffled?")
            # TODO: user input
            deck.shuffleDeck()
        elif(self.role == ' cutter'):
            # TODO: message for cutter
            print("How many cards do you want to cut?")
            deck.cutDeck()
            # TODO: user input
        elif(self.role == 'dealer'):
            # TODO: message for dealer
            print("Do you want to take the top card or the bottom card?")
            # TODO: user input
            decision = 'Top'  # this is the user input
            if(decision == 'Top'):
                self.hand.append(deck.card.pop(0))
                return self.hand[0].getSuit()
            elif(decision == 'Bottom'):
                self.hand.append(deck.card.pop())
                return self.hand[0].getSuit()
            else:
                # Server message to client
                print('Wrong input')
        else:
            print("Waiting for players do perform their tasks...")


class Team:
    """ This class is responsible for the team dynamics"""

    def __init__(self):
        self.players = []
        self._points = 0
        self._roundsWon = 0
        self._cardsInStack = []

    def addCards(self, cards):
        self._cardsInStack.append(*[cards])

    def getPoints(self):
        return self._points

    def addPlayer(self, p):
        self.players.append(p)

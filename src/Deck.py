import json
from Card import Card
import random
import os


class Deck:

    """ This class applies sall the functionality of a sueca deck"""

    def __init__(self):
        self.cards = []
        dirname = os.path.dirname(__file__)

        with open(os.path.join(dirname, 'deck.json')) as json_file:
            data = json.load(json_file)
            buffer = data['buffer']
            for p in data['deck']:
                suit = p['suit']
                value = p['number']
                self.cards.append(Card(suit, value, buffer))

    def shuffleDeck(self, times=1):
        for n in range(times):
            x = [i for i in self.cards]
            random.shuffle(x)
            self.cards = (x)

    def cutDeck(self, percentage=0):
        # Always from top to bottom
        cardsToMove = round(len(self.cards) * percentage)
        sliceObj = slice(cardsToMove)
        self.cards = [
            *self.cards[cardsToMove:len(self.cards)], *self.cards[sliceObj]]
        print('control')

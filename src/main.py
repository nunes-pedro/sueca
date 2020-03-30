from Deck import Deck
from Player import Player
from Table import Table
import jsonpickle


def main():

    deck = Deck()
    p1 = Player()
    p1.getHand(deck)
    p2 = Player()
    p2.getHand(deck)
    p3 = Player()
    p3.getHand(deck)
    p4 = Player()
    p4.getHand(deck)
    pjson = jsonpickle.encode(p4)
 #   deck.shuffleDeck(2)
 #   deck.cutDeck(.98)
    t = Table()
    points = t.getPoints('A')
    t.sitPlayer(p1)
    t.sitPlayer(p2)
    t.sitPlayer(p3)
    t.sitPlayer(p4)

    tJson = jsonpickle.encode(t)
    test = jsonpickle.decode(tJson)
    print("control")


if __name__ == "__main__":
    main()

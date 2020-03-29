from Deck import Deck
from Player import Player
from Table import Table


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
 #   deck.shuffleDeck(2)
 #   deck.cutDeck(.98)
    t = Table()
    points = t.getPoints('A')
    t.sitPlayer(p1)
    t.sitPlayer(p2)
    t.sitPlayer(p3)
    t.sitPlayer(p4)

    print("control")


if __name__ == "__main__":
    main()

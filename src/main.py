from Deck import Deck
from Player import Player


def main():

    deck = Deck()
    player = Player('dealer', 1)
    player.getHand(deck)
 #   deck.shuffleDeck(2)
 #   deck.cutDeck(.98)

    print("control")


if __name__ == "__main__":
    main()

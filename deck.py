import random




class Card:

    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    SUITS = ["♣", "♦", "♥", "♠"]


    def __init__(self, suit, rank):
        """
        init card w/ suit n rank
        """
        if rank not in self.RANKS:
            raise ValueError("Invalid rank")
        if suit not in self.SUITS:
            raise ValueError("Invalid suit")
        self._suit = suit
        self._rank = rank


    def __str__(self):
        """
        str rep of card
        """
        return f"{self._rank}{self._suit}"

    def __repr__(self):
        """
        str rep for lists n stuff
        """
        return self.__str__()




    @property
    def suit(self):
        """
        get card suit
        """
        return self._suit


    @property
    def rank(self):
        """
        get card rank
        """
        return self._rank




class Deck:
    def __init__(self):
        """
        make a deck of 52 cards
        """
        self._deck = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self._deck.append(Card(suit, rank))

    def __str__(self):
        """
        str rep of whole deck
        """
        return str(self._deck)


    def shuffle(self):
        """
        shuffle deck
        """
        random.shuffle(self._deck)

    def deal(self):
        """
        deal the top card
        """
        return self._deck.pop(0)

if __name__ == "__main__":
    deck = Deck()
    print(deck)
    deck.shuffle()
    print(deck)
    print(deck.deal())

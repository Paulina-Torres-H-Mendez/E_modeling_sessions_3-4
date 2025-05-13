from deck import Deck, Card   # <- assumes you already have these classes

class PokerHand:
    """
    A five-card poker hand that knows how to check for a **flush**.
    """

    def __init__(self, deck: Deck):
        """
        Constructor. As soon as you make a PokerHand, it:
        1. Draws 5 cards off the supplied `deck`.
        2. Stores them internally so other methods can use them later.
        """
        cards = []
        for _ in range(5):          # repeat exactly 5 times
            cards.append(deck.deal())
        self._cards = cards         # leading underscore = “please treat as private”

    @property
    def cards(self):
        """
        Neat, read-only accessor.
        Lets you do `hand.cards` instead of the clunkier `hand._cards`.
        """
        return self._cards

    def __str__(self):
        """
        When you do `print(hand)` Python calls this.
        It simply turns the list of Card objects into a readable string,
        e.g.  "[K♠, 10♠, 7♠, 6♠, 2♠]".
        """
        return str(self.cards)

    @property
    def is_flush(self):
        """
        Returns **True** if **every** card has the same suit.
        Logic: compare the suit of each card (indices 1-4) against the
        suit of the very first card (index 0). One mismatch → not a flush.
        """
        first_suit = self.cards[0].suit
        for card in self.cards[1:]:
            if card.suit != first_suit:
                return False
        return True

# ------------------------------------------------------------------
# Monte-Carlo loop: keep dealing hands until we’ve seen 1 000 flushes
# ------------------------------------------------------------------
count    = 0      # total hands dealt
flushes  = 0      # how many of those were flushes

while flushes < 1000:
    deck = Deck()
    deck.shuffle()
    hand = PokerHand(deck)

    if hand.is_flush:
        flushes += 1
    count += 1
print(f"Probability of a flush is {100 * flushes / count:.4f}%")
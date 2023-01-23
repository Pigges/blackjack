# Import
import sys, random
from classes import Card
from classes.card import cards

class Deck:
    def __init__(self, sets) -> None:
        """
        The class for the Deck

        @param  {Int}   sets    Number of sets the Deck will consist of
        """

        self.sets = sets
        self.cards = createDeck(self.sets) # Create Cards in Deck
        self.shuffle() # Shuffle the Cards

    def resetShuffle(self):
        """
        Reset and shuffle the Deck
        """

        self.cards = createDeck(self.sets)
        self.shuffle()

    def shuffle(self):
        """
        Shuffle the Deck
        """

        random.shuffle(self.cards); # Shuffle the Cards

    def draw(self):
        """
        Draw a Card from the deck

        @return Card: Object
        """

        card = self.cards[0]
        self.cards.pop(0)

        return card

def createDeck(sets):
    """
    Create a full Deck of cards with x number of sets

    @param  {Int}   sets    Number of sets the Deck will consist of
    @return Array: All the Cards in a list
    """

    cardList = []

    # Loop creating x sets
    for set in range(sets):
        # Loop through all card suites
        for suite in cards['suites']:
            # Loop through all card values
            for value in range(len(cards['names'])):
                # Create and append the Card to the cardList
                cardList.append(Card(value, cards['names'][value], suite))

    return cardList

sys.modules[__name__] = Deck
import sys

class Card:
    def __init__(self, value, name, suit) -> None:
        """
        The class for the Card

        @param  {Int}       value   How many points the card represents
        @param  {String}    name    The name of the card
        @param  {String}    suit    The name of the suit the card is part of
        """
        self.value = value + 1
        self.name = name
        self.suit = suit

        if self.value > 10:
            self.value = 10

    def getValue(self, score) -> int:
        """
        Determine the value the card will return

        @param  {Int}   score   The current score for the player
        @return {Int}           The value the card determined to be having
        """

        if self.value == 1 and score + self.value <= 21:
            return 11
        else:
            return self.value

    def __str__(self) -> str:
        """
        When printing the Object, return the what card it is.
        Format: {name} of {suit}

        @return {String}        Returns what card it is
        """

        return f"{self.name} of {self.suit}"

sys.modules[__name__] = Card
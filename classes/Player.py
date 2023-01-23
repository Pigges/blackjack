import sys

class Player:
    def __init__(self, name) -> None:
        """
        The class for the Player

        @param  {String}    name    The name of the player
        """

        self.name = name
        self.hand = [] # List of Cards that the Player have drawn
        self.lastDrawnCard = None # The last drawn Card
        self.score = 0 # Current score

    def __str__(self):
        return f"{self.name} currently have a score of {self.score}"

    def reset(self):
        self.hand = []
        self.lastDrawnCard = None
        self.score = 0
        
sys.modules[__name__] = Player
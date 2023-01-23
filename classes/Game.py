# Imports
import sys
from classes import Player
from classes import Deck

class Game:
    def __init__(self, name) -> None:
        """
        Initialize the Game.

        @param  {String}    name    The name of the player
        """

        self.player = Player(name)
        self.dealer = Player("Dealer")
        self.deck = Deck(4)
        self.__start()

    def __start(self):
        input("Press ENTER when you are ready: ")
        self.playerDrawCard(self.dealer, True)
        self.playerDrawCard(self.player, True)
        self.playerDrawCard(self.dealer)
        self.playerDrawCard(self.player, True)

        print(f"\n{self.player}")
    
    def game(self, fn):
        """
        The main game loop. This will keep calling the function entered until it returns true

        @param  {Function}  fn  The function to call
        """
        while True:
            if fn():
                break
            
        answer = input("\n\nDo you want to play again? [y/N]")
        if answer.lower() == 'y':
            print("Game is reset!\n\n")
            self.reset()
            return self.game(fn)
        
        print("See you!")

    def reset(self):
        """
        This will reset the game if the player wants to start over
        """

        self.player.reset()
        self.dealer.reset()
        self.deck.resetShuffle()
        self.__start()
    
    def playerDrawCard(self, player, show=False):
        """
        The method to draw a Card for the entered player

        @param  {Boolean}   show    Whether or not to show what Card got drawn
        """

        player.lastDrawnCard = self.deck.draw()
        player.hand.append(player.lastDrawnCard)
        player.score += player.lastDrawnCard.getValue(player.score)

        if show:
            print(f"{player.name} draw a {self.dealer.lastDrawnCard}.")
        else:
            print(f"{player.name} draw an unknown card.")

sys.modules[__name__] = Game
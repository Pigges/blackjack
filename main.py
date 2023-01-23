# Import
import time
from classes import Game

# Welcome message
print("""
************************************
*     Welcome to the BlackJack     *
************************************

    Think you can beat this game?\n\n""")

game = Game(input("Choose a name: "))

# Main game loop
def main():
    if game.player.score > 21:
        print("You got a score over 21 and lost the game.")
        return True
    elif game.player.score == 21:
        print("You got 21 and win the game.")
        return True
    
    answer = input("Are you done [y/N]: ")
    if answer.lower() == 'y':
        handleDealerDraw()
        handleGameWin()
        return True
        
    game.playerDrawCard(game.player, True)


def handleDealerDraw():
    while game.dealer.score < 17:
        time.sleep(0.5)
        game.playerDrawCard(game.dealer, True)
        
    print(game.dealer)
    
# Handle win scenarios
def handleGameWin():
    if game.dealer.score == 21:
        print("The dealer got a score of 21 and thereby win the game.")
    elif game.dealer.score > 21:
        print("The dealer got a score of more than 21 and thereby you win the game.")
    elif game.dealer.score > game.player.score:
        print("The dealer got a higher score than you and thereby win the game.")
    elif game.dealer.score == game.player.score:
        print("Both the dealer and you got the same score and thereby it is a tie")
    elif game.dealer.score < game.player.score:
        print("You got a higher score and thereby win the game.")
        
    return True

game.game(main)
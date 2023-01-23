# Blackjack en Python

## Structure
* [x] First I load the card types and value names into a dictionary for later use.

* [x] Next up is the [Card](#card) class which should handle a card with its value, suit and name. It should have a method which handles the score it will give when it gets drawn. This is because it should handle whether or not the Ace card should be worth 1 or 11. Therefore this method needs to receive the current score in order to know if the score will get over 21, so it can return 1 if that is the case. You should also be able to print the object in order to get the name of the card. E.g. `Ace of Hearts`

* [x] Now it's time for the [Deck](#deck) class. This will now include x numbers of full sets of cards. The only parameter this class would need then is just simply the number of sets it needs to generate. The methods this class needs would be to reset the deck for a rematch, and a shuffle method which would just simply shuffle the order of the cards. As well as the method to actually draw a card.

* [x] Now the [Player](#player) class should be implemented. The player should have the following properties:
    * Hand: List (List of all the cards that the player have received)
    * LastDrawnCard: Card (The last drawn card)
    * Score: int (Current score)

    It should also contain a method to reset the player to "factory settings". You should also be able to print the object and get a text of the current score.

* [x] The [Game](#game) class should be the main object which contains all the subclasses, and the one which initializes the whole game.



## Class diagrams
### Card
```python
__init__(value: int, suit: suitType)
    Value: int
    Name: String
    Suit: suitType

value(Score: int)
    # If Value == 1
        # Check whether the result score would reach 21 or not
        # If end_score > 21: return = 1
        # Else: return = 11
    # If Value > 10
        # return = 10
    return: int

__str__()
    return: String
```

### Deck
```python
__init__(NrOfDecks: int)
    Cards: list

resetShuffle()
    # reset deck and shuffle

shuffle()
    # shuffle deck

draw()
    return: Card
```

### Player
```python
__init__()
    Hand: list
    LastDrawnCard: Card
    Score: int
    LowValue: int
    HighValue: int
    BestValue: int

Reset()
    # reset Player

__str__()
    return: String
```

### Game
```python
__init__()
    Player: Player
    Dealer: Player
    Deck: Deck
    Status: String (Won, Lost, Playing, Tie, Blackjack)

Game():
    # The main game loop

Reset():
    # Handles game reset

PlayerDraw(player):
    # Handle player drawing a card (Player, Dealer)
```
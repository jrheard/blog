# TODO: delete this comment and put your name here.



def print_game_status(player_hand, player_count, dealer_hand, dealer_count, deck):
    """A function that prints out the state of the game.

    Call this function whenever the state of the game changes (e.g. after the player
    and dealer get their opening hand; whenever the player draws another card; etc.)
    """
    print("------------------------------------")
    print("Your hand: {0}".format(player_hand))
    print("Your count: {0}".format(player_count))
    print("Dealer's hand: {0}".format(dealer_hand))
    print("Dealer's count: {0}".format(dealer_count))
    print("Number of cards in deck: {0}".format(len(deck)))
    print("------------------------------------")





# TODO: Create a deck of cards and shuffle it.
#       Use a variable named `deck` to store a list of cards.

# TODO: Deal two cards to the player.
#       Use a list variable named  `player_hand` and an integer variable named `player_count`.

# TODO: Deal two cards to the dealer.
#       Use a list variable named `dealer_hand` and an integer variable named `dealer_count`.

# TODO: Implement the player's turn.
#
#       TODO: ask them if they want to "hit" or "stand".
#
#       TODO: If the player says "hit": remove a card from the deck,
#       add it to the player's hand, and update their count.
#
#       TODO: Once you've done that, print out
#       the current state of the game so that
#       the player can see their new hand and count.
#
#       TODO: If the player's count is greater than 21, they lost!
#       End their turn and skip the dealer's turn.

# TODO: Implement the dealer's turn.

# TODO: Print out who won! Remember, we're running an automated testing
#       program on your code, so the last line of your program's output
#       MUST be one of these _exact_ strings:
#           - If the dealer busts: "Dealer busts, you won!"
#           - If the player won: "You won!"
#           - If there is a tie: "It's a tie!"
#           - If the player lost: "You lost!"


# Have fun!

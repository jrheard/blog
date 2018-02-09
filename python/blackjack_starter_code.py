# Here's a function you can use in order to print out the current state of the game.
# You can use this function like this:
#
#     print_game_status(player_hand, dealer_hand, deck)

def print_game_status(player_hand, dealer_hand, deck):
    # This function prints out something like:
    #
    #    Your hand: [[9, 'hearts'], [1, 'spades']]
    #    Your count: 10
    #    Dealer's hand: [[4, 'spades'], [4, 'hearts']]
    #    Dealer's count: 8
    #    Number of cards in deck: 48

    print("Your hand: {0}".format(player_hand))
    hand_value = sum(value for (value, _) in hand)
    print("Your count: {0}".format(hand_value))

    print("Dealer's hand: {0}".format(dealer_hand))
    dealer_hand_value = sum(value for (value, _) in dealer_hand)
    print("Dealer's count: {0}".format(dealer_hand_value))

    print("Number of cards in deck: {0}".format(len(deck)))




# TODO: Create a deck of cards and shuffle it.
deck = []

# TODO: Deal two cards to the player.
player_hand = []

# TODO: Deal two cards to the dealer.
dealer_hand = []

# TODO: Implement the player's turn.

# TODO: Implement the dealer's turn.

# TODO: Print out who won!

# The last line of your program's output MUST be one of these exact messages:

# If the dealer busts, use this line:
# print("Dealer busts, you won!")

# If the player's count is higher than the dealer's, use this line:
# print("You won!")

# If the player's count is equal to the dealer's, use this line:
# print("It's a tie!")

# If the player lost, use this line:
# print("You lost!")

# Remember, we're running an automated testing program on your code,
# and it'll be looking for those _exact_ messages.




# Have fun!

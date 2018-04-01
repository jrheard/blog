import random

import crayons

PLAYER = 'player'
COMPUTER = 'computer'


# Here are the empty functions that it's your job to implement!

def make_board():
    pass


def get_computer_move(board):
    pass


def print_board(board):
    pass


def get_player_move():
    pass


def check_for_winner(board):
    pass


# Now that we've defined our functions, let's play a game of tic-tac-toe!


# (Note: This `if` statement is important, please don't remove it.)
if __name__ == '__main__':

    print('Welcome to Tic-Tac-Toe!')

    # Ask the player what team they want to be.
    player_team = input('Do you want to be X or O?\n').upper()

    if player_team == 'X':
        computer_team = 'O'
    else:
        computer_team = 'X'

    # Decide who goes first.
    whose_turn = random.choice([PLAYER, COMPUTER])
    print('The {} will go first.'.format(whose_turn))

    # Get a fresh board.
    board = make_board()

    while True:
        # Figure out whose turn it is, and let them make a move.
        if whose_turn == PLAYER:
            print_board(board)
            x, y = get_player_move()
            board[x][y] = player_team

        else:
            x, y = get_computer_move(board)
            board[x][y] = computer_team

        # Check to see if someone won, and end the game if so.
        winner = check_for_winner(board)
        if winner:
            print('-------------------')

            if winner == 'tie':
                print("It's a tie!")
            else:
                print('The {} wins!'.format(whose_turn))

            print_board(board)
            break

        # If we've made it this far, nobody's won yet, so let's get ready for the next turn.
        if whose_turn == PLAYER:
            whose_turn = COMPUTER
        else:
            whose_turn = PLAYER

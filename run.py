# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from random import randint

board = []

for _ in range(6):
    board.append(["O"] * 6)


def print_board(board):
    for row in board:
        print(" ".join(row))


print("Battleship Game")
print_board(board)


def random_row(board):
    return randint(0, len(board) - 1)


def random_column(board):
    return randint(0, len(board[0]) - 1)


ship_row = random_row(board)
ship_column = random_column(board)


while True:
    print("Attack!")
    guess_row = input("Guess Row (0-5): ")
    guess_column = input("Guess Column (0-5): ")

    if guess_row.isdigit() and guess_column.isdigit():
        guess_row = int(guess_row)
        guess_column = int(guess_column)

        if guess_row == ship_row and guess_column == ship_column:
            print("Congratulations! You sunk the battleship!")
            break
        else:
            if guess_row not in range(6) or guess_column not in range(6):
                print("Please enter a number between 0 and 5.")
            elif board[guess_row][guess_column] == "X":
                print("Please enter a number that you haven't already guessed.")
            else:
                print("You missed the battleship!")
                board[guess_row][guess_column] = "X"
    else:
        print("Please enter a number between 0 and 5.")

    print_board(board)

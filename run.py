from random import randint

board_size = 6

def create_board():
    board = []
    for _ in range(board_size):
        board.append(["O"] * board_size)
    return board

def print_boards(player_board, computer_board):
    print("\nYour Board:")
    for row in player_board:
        print(" ".join(row))
    print("\nComputer's Board:")
    for row in computer_board:
        print(" ".join(row))

def random_row(board):
    return randint(0, len(board) - 1)

def random_column(board):
    return randint(0, len(board[0]) - 1)

def play_game():
    print("Battleship Game")

    player_board = create_board()
    computer_board = create_board()

    player_ship_row = random_row(player_board)
    player_ship_column = random_column(player_board)

    computer_ship_row = random_row(computer_board)
    computer_ship_column = random_column(computer_board)

    print("Your Battleship Location: Row:", player_ship_row, "Column:", player_ship_column)

    while True:
        print_boards(player_board, computer_board)

        valid_input = False
        while not valid_input:
            player_guess_row = input("Guess Row (0-5): ")
            player_guess_column = input("Guess Column (0-5): ")

            if player_guess_row.isdigit() and player_guess_column.isdigit():
                player_guess_row = int(player_guess_row)
                player_guess_column = int(player_guess_column)

                if player_guess_row in range(board_size) and player_guess_column in range(board_size):
                    valid_input = True
                else:
                    print("Please enter a number between 0 and", board_size - 1)
            else:
                print("Please enter a number between 0 and 5")

        if player_guess_row == computer_ship_row and player_guess_column == computer_ship_column:
            print("You hit the computer's battleship!")
            computer_board[player_guess_row][player_guess_column] = "X"
            break
        else:
            if computer_board[player_guess_row][player_guess_column] == "X":
                print("Please enter a position that you haven't already guessed")
            else:
                print("\nYour Turn:")
                print("You missed the computer's battleship!")
                computer_board[player_guess_row][player_guess_column] = "X"

        print("\nComputer's Turn:")

        computer_guess_row = random_row(player_board)
        computer_guess_column = random_column(player_board)

        if (
            computer_guess_row == player_ship_row
            and computer_guess_column == player_ship_column
        ):
            print("Oh no! Computer sunk your battleship!")
            player_board[computer_guess_row][computer_guess_column] = "X"
            break
        else:
            if player_board[computer_guess_row][computer_guess_column] == "X":
                continue  # Computer already guessed this position, try again
            else:
                print("Computer missed your battleship!")
                player_board[computer_guess_row][computer_guess_column] = "X"

play_game()

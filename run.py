from random import randint
from colorama import init, Fore


class BattleshipGame:
    def __init__(self):
        self.board_size = 6  # Default grid size
        self.player_board = []
        self.computer_board = []
        self.player_ships = []
        self.computer_ships = []
        self.guessed_positions = set()
        init()  # Initialize Colorama

    def set_grid_size(self):
        # Prompts the user to enter the desired grid size
        while True:
            try:
                size = int(input("Enter the grid size (minimum 5, maximum 20): "))
                if 5 <= size <= 20:
                    self.board_size = size
                    break
                else:
                    print("Grid size should be between 5 and 20.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def create_board(self):
        # Creates an empty game board
        board = []
        for _ in range(self.board_size):
            board.append(["O"] * self.board_size)
        return board

    def place_ships(self, board, num_ships):
        # Randomly places ships on the game board
        ships = []
        for _ in range(num_ships):
            ship_row = randint(0, self.board_size - 1)
            ship_column = randint(0, self.board_size - 1)
            while board[ship_row][ship_column] != "O":
                ship_row = randint(0, self.board_size - 1)
                ship_column = randint(0, self.board_size - 1)
            board[ship_row][ship_column] = "S"
            ships.append((ship_row, ship_column))
        return ships

    def print_boards(self):
        # Prints the current game boards (player's and computer's)
        print("\nYour Board:")
        for row in self.player_board:
            print(" ".join(row))
        print("\nComputer's Board:")
        for row in self.computer_board:
            print(
                " ".join(
                    [
                        Fore.RED + "X" + Fore.RESET if cell == "X" else "O"
                        for cell in row
                    ]
                )
            )

    def update_board(self, board, row, column, value):
        # Updates a specific position on the game board with the provided value
        board[row][column] = value

    def play_game(self):
        print("Battleship Game")

        self.set_grid_size()
        self.player_board = self.create_board()
        self.computer_board = self.create_board()
        self.player_ships = self.place_ships(self.player_board, 3)
        self.computer_ships = self.place_ships(self.computer_board, 3)

        while True:
            self.print_boards()

            valid_input = False
            while not valid_input:
                try:
                    player_guess_row = int(
                        input("Guess Row (0-{}): ".format(self.board_size - 1))
                    )
                    player_guess_column = int(
                        input("Guess Column (0-{}): ".format(self.board_size - 1))
                    )

                    if player_guess_row in range(
                        self.board_size
                    ) and player_guess_column in range(self.board_size):
                        position = (player_guess_row, player_guess_column)
                        if position not in self.guessed_positions:
                            self.guessed_positions.add(position)
                            valid_input = True
                        else:
                            print(
                                "You have already guessed that position. Please enter a new one."
                            )
                    else:
                        print(
                            "Please enter a number between 0 and {}".format(
                                self.board_size - 1
                            )
                        )
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

            if (player_guess_row, player_guess_column) in self.computer_ships:
                print(Fore.GREEN + "\nYou hit the computer's battleship!" + Fore.RESET)
                self.update_board(
                    self.computer_board, player_guess_row, player_guess_column, "X"
                )
                self.computer_ships.remove((player_guess_row, player_guess_column))
                if len(self.computer_ships) == 0:
                    print(
                        Fore.GREEN
                        + "Congratulations! You sank all of the computer's battleships. You win!"
                        + Fore.RESET
                    )
                    break
            else:
                if self.computer_board[player_guess_row][player_guess_column] == "X":
                    print("Please enter a position that you haven't already guessed")
                else:
                    print("\nYou missed the computer's battleship!")
                    self.update_board(
                        self.computer_board, player_guess_row, player_guess_column, "X"
                    )

            computer_guess_row = randint(0, self.board_size - 1)
            computer_guess_column = randint(0, self.board_size - 1)

            if (computer_guess_row, computer_guess_column) in self.player_ships:
                print(
                    Fore.RED
                    + "Oh no! Computer sunk one of your battleships!"
                    + Fore.RESET
                )
                self.update_board(
                    self.player_board, computer_guess_row, computer_guess_column, "X"
                )
                self.player_ships.remove((computer_guess_row, computer_guess_column))
                if len(self.player_ships) == 0:
                    print(
                        Fore.RED
                        + "All of your battleships have been sunk. You lose!"
                        + Fore.RESET
                    )
                    break
            else:
                if self.player_board[computer_guess_row][computer_guess_column] == "X":
                    continue  # Computer already guessed this position, try again
                else:
                    print("Computer missed your battleship!")
                    self.update_board(
                        self.player_board,
                        computer_guess_row,
                        computer_guess_column,
                        "X",
                    )


game = BattleshipGame()
game.play_game()

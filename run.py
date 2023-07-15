from random import randint


class BattleshipGame:
    def __init__(self, board_size):
        self.board_size = board_size
        self.player_board = self.create_board()
        self.computer_board = self.create_board()
        self.player_ships = []
        self.computer_ships = []
        self.guessed_positions = set()  # Keep track of guessed positions

    def create_board(self):
        board = []
        for _ in range(self.board_size):
            board.append(["O"] * self.board_size)
        return board

    def place_ships(self, board, num_ships):
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
        print("\nYour Board:")
        for row in self.player_board:
            print(" ".join(row))
        print("\nComputer's Board:")
        for row in self.computer_board:
            print(" ".join(["X" if cell == "X" else "O" for cell in row]))

    def update_board(self, board, row, column, value):
        board[row][column] = value

    def play_game(self):
        print("Battleship Game")

        self.player_ships = self.place_ships(self.player_board, 3)
        self.computer_ships = self.place_ships(self.computer_board, 3)

        while True:
            self.print_boards()

            valid_input = False
            while not valid_input:
                player_guess_row = input("Guess Row (0-5): ")
                player_guess_column = input("Guess Column (0-5): ")

                if player_guess_row.isdigit() and player_guess_column.isdigit():
                    player_guess_row = int(player_guess_row)
                    player_guess_column = int(player_guess_column)

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
                            "Please enter a number between 0 and", self.board_size - 1
                        )
                else:
                    print("Please enter a number between 0 and 5")

            if (player_guess_row, player_guess_column) in self.computer_ships:
                print("\nYou hit the computer's battleship!")
                self.update_board(
                    self.computer_board, player_guess_row, player_guess_column, "X"
                )
                self.computer_ships.remove((player_guess_row, player_guess_column))
                if len(self.computer_ships) == 0:
                    print(
                        "Congratulations! You sank all of the computer's battleships. You win!"
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
                print("Oh no! Computer sunk one of your battleships!")
                self.update_board(
                    self.player_board, computer_guess_row, computer_guess_column, "X"
                )
                self.player_ships.remove((computer_guess_row, computer_guess_column))
                if len(self.player_ships) == 0:
                    print("All of your battleships have been sunk. You lose!")
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


game = BattleshipGame(6)
game.play_game()

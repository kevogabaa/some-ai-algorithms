import math


class TicTacToe:
    """A class to represent a Tic Tac Toe game."""

    def __init__(self):
        """Constructs a new instance of Tic Tac Toe game.

        Initializes an empty board.
        """
        self.board = [" " for _ in range(9)]  # Representing board as a list

    def print_board(self):
        """Prints the current state of the board."""
        for row in [self.board[i * 3 : (i + 1) * 3] for i in range(3)]:  # NOQA: E203
            print("| " + " | ".join(row) + " |")

    def available_moves(self):
        """Returns a list of available moves."""
        return [i for i, spot in enumerate(self.board) if spot == " "]

    def num_empty_squares(self):
        """Returns the number of empty squares on the board."""
        return self.board.count(" ")

    def make_move(self, position, player):
        """Makes a move on the board."""
        # check if the move is valid
        self.board[position] = player

    def check_winner(self, player):
        """Checks if the given player has won the game."""
        # Check rows, columns, and diagonals
        winning_positions = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],  # rows
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],  # columns
            [0, 4, 8],
            [2, 4, 6],  # diagonals
        ]
        for positions in winning_positions:
            if all(self.board[p] == player for p in positions):
                return True
        return False

    def evaluate_board(self):
        """Evaluates the board and returns a score."""
        if self.check_winner("X"):
            return 1
        elif self.check_winner("O"):
            return -1
        else:
            return 0

    def alphabeta(self, alpha, beta, depth, player):
        """Implements the Alpha-Beta pruning algorithm for decision making."""
        if depth == 0 or self.num_empty_squares() == 0:
            return self.evaluate_board()

        if player == "X":  # Maximizing player
            max_eval = -math.inf
            for move in self.available_moves():
                self.make_move(move, player)
                eval = self.alphabeta(alpha, beta, depth - 1, "O")  # Switch to opponent's turn
                self.make_move(move, " ")  # Undo move
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:  # Minimizing player
            min_eval = math.inf
            for move in self.available_moves():
                self.make_move(move, player)
                eval = self.alphabeta(
                    alpha, beta, depth - 1, "X"
                )  # Switch to maximizing player's turn
                self.make_move(move, " ")  # Undo move
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval

    def best_move(self, player, depth):
        """Returns the best move for the given player."""
        best_eval = -math.inf if player == "X" else math.inf
        best_move = None
        alpha = -math.inf
        beta = math.inf
        for move in self.available_moves():
            self.make_move(move, player)
            eval = (
                self.alphabeta(alpha, beta, depth, "O")
                if player == "X"
                else self.alphabeta(alpha, beta, depth, "X")
            )
            self.make_move(move, " ")
            if (player == "X" and eval > best_eval) or (player == "O" and eval < best_eval):
                best_eval = eval
                best_move = move
        return best_move

    def play(self, depth=10):
        """Starts the game and continues until there is a winner or a tie."""
        current_player = "X"
        while True:
            self.print_board()
            if self.check_winner("X"):
                print("X wins!")
                break
            elif self.check_winner("O"):
                print("O wins!")
                break
            elif self.num_empty_squares() == 0:
                print("It's a tie!")
                break

            if current_player == "X":
                while True:
                    try:
                        move = int(input("Enter your move (0-8): "))
                        if move in range(9) and self.board[move] == " ":
                            break
                        else:
                            error = (
                                "between 0 and 8 that corresponds to an empty spot on the board."
                            )
                            print(f"Invalid move. Please enter a number {error}")
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                self.make_move(move, current_player)
            else:
                print("Computer's turn...")
                move = self.best_move(current_player, depth)
                self.make_move(move, current_player)
            current_player = "O" if current_player == "X" else "X"


def main():
    """The main function to start the game."""
    # Usage
    depth = int(input("Enter the depth for the Minimax algorithm (default is 10): "))
    game = TicTacToe()
    game.play(depth) if depth > 10 else game.play()


if __name__ == "__main__":
    main()

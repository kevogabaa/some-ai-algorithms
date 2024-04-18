import time


def is_safe(board, row, col):
    """Check if it is safe to place a queen at a given position on the board.

    Parameters:
    - board (list of lists): The current state of the chessboard.
    - row (int): The row index of the position being checked.
    - col (int): The column index of the position being checked.

    Returns:
    - bool: True if it is safe to place a queen, False otherwise.
    """
    # Check if placing a queen at board[row][col] is safe
    n = len(board)

    # Check the row
    if any(board[row][c] == 1 for c in range(n)):
        return False

    # Check the column
    if any(board[r][col] == 1 for r in range(n)):
        return False

    # Check upper-left diagonal
    r, c = row, col
    while r >= 0 and c >= 0:
        if board[r][c] == 1:
            return False
        r -= 1
        c -= 1

    # Check upper-right diagonal
    r, c = row, col
    while r >= 0 and c < n:
        if board[r][c] == 1:
            return False
        r -= 1
        c += 1

    return True


def eliminate_row(board, row, col):
    """Eliminate conflicting values in the same row."""
    n = len(board)
    board[row] = [0 if c != col else 1 for c in range(n)]


def eliminate_column(board, row, col):
    """Eliminate conflicting values in the same column."""
    n = len(board)
    for r in range(n):
        if r != row:
            board[r][col] = 0


def eliminate_diagonal(board, row, col):
    """Eliminate conflicting values in the diagonal."""
    n = len(board)
    r, c = row - 1, col - 1
    while r >= 0 and c >= 0:
        board[r][c] = 0
        r -= 1
        c -= 1
    r, c = row - 1, col + 1
    while r >= 0 and c < n:
        board[r][c] = 0
        r -= 1
        c += 1


def arc_consistency(board):
    """Enforce arc consistency on the board."""
    n = len(board)
    for row in range(n):
        for col in range(n):
            if board[row][col] == 1:
                eliminate_row(board, row, col)
                eliminate_column(board, row, col)
                eliminate_diagonal(board, row, col)


def solve(board, row):
    """Recursively solve the N-Queens problem.

    Parameters:
    - board (list of lists): The current state of the chessboard.
    - row (int): The current row being considered for queen placement.

    Returns:
    - bool: True if a solution is found, False otherwise.
    """
    n = len(board)
    if row == n:
        return True

    for col in range(n):
        if is_safe(board, row, col):
            board[row][col] = 1
            arc_consistency(board)  # Enforce arc consistency
            if solve(board, row + 1):
                return True
            board[row][col] = 0

    return False


def print_solution(board):
    """Print the solution of the N-Queens problem.

    Parameters:
    - board (list of lists): The final state of the chessboard after solving the problem.
    """
    for row in board:
        print(" ".join("Q" if cell == 1 else "." for cell in row))


def main():
    """Main function to solve the N-Queens problem."""
    n = int(input("Enter the number of queens: "))
    if n < 1:
        print("Invalid input. Please enter a positive integer.")
        return

    board = [[0] * n for _ in range(n)]
    print(board)
    start_time = time.monotonic()
    if solve(board, 0):
        print("Solution:")
        print_solution(board)
        print("Solved in %.6f seconds" % (time.monotonic() - start_time))
    else:
        print("No solution found.")


if __name__ == "__main__":
    main()

import time

import numpy as np

grid = [
    [0, 3, 5, 9, 0, 0, 0, 8, 0],
    [0, 0, 8, 5, 0, 3, 0, 0, 0],
    [6, 0, 2, 7, 0, 0, 3, 9, 0],
    [0, 8, 9, 0, 5, 0, 0, 4, 0],
    [2, 7, 0, 0, 0, 0, 0, 1, 3],
    [0, 6, 0, 0, 3, 0, 8, 7, 0],
    [0, 1, 6, 0, 0, 5, 9, 0, 4],
    [0, 0, 0, 8, 0, 6, 1, 0, 0],
    [0, 5, 0, 0, 0, 9, 6, 3, 0],
]


def possible(y, x, n):
    """Checks if placing the number 'n' at position (y, x) on the Sudoku grid is valid.

    Args:
        y (int): Row index.
        x (int): Column index.
        n (int): Number to be placed.

    Returns:
        bool: True if 'n' can be placed at (y, x), False otherwise.
    """
    global grid
    for i in range(0, 9):
        if grid[y][i] == n:
            return False
    for i in range(0, 9):
        if grid[i][x] == n:
            return False
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[y0 + i][x0 + j] == n:
                return False

    return True


possible(4, 4, 3)


def solve():
    """Solves a Sudoku puzzle using recursive backtracking.

    The function iterates through each cell in the grid. If the cell is empty (contains 0), it
    tries placing numbers from 1 to 9 in that cell. For each number, it checks if it's possible to
    place that number in the current cell using the `possible()` function. If a valid number is
    found, it places it in the cell and recursively calls `solve()` to continue solving the rest of
    the puzzle. If no valid number can be placed, it backtracks by resetting the cell value to 0.
    When the entire grid is filled, it prints the solved Sudoku grid.
    """
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if possible(y, x, n):

                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0
                return
    print(np.matrix(grid))


def main():
    start = time.monotonic()
    solve()
    t = time.monotonic() - start
    print("Solved: %.5f sec" % t)


if __name__ == "__main__":
    main()

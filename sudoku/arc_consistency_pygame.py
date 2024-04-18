import sys
import time

import pygame
from arc_consistency import random_puzzle, solve, squares

# Define some constants
WINDOW_SIZE = 600
GRID_SIZE = 9
CELL_SIZE = WINDOW_SIZE // GRID_SIZE
LINE_WIDTH = 2
FONT_SIZE = CELL_SIZE // 2

# Initialize Pygame
pygame.init()

# Set up some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the display
window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))

# Set up the font
font = pygame.font.Font(None, FONT_SIZE)


def draw_grid():
    for i in range(GRID_SIZE):
        pygame.draw.line(
            window, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, WINDOW_SIZE), LINE_WIDTH
        )
        pygame.draw.line(
            window, BLACK, (0, i * CELL_SIZE), (WINDOW_SIZE, i * CELL_SIZE), LINE_WIDTH
        )


def draw_numbers(grid):
    for i, row in enumerate(grid):
        for j, num in enumerate(row):
            if num != 0:
                text = font.render(str(num), True, BLACK)
                window.blit(text, (j * CELL_SIZE + CELL_SIZE // 3, i * CELL_SIZE))


def main():
    # Generate a random Sudoku puzzle
    puzzle = random_puzzle()

    # Convert the puzzle to a 2D list format that the GUI can understand
    grid = [
        [
            int(puzzle[i * GRID_SIZE + j]) if puzzle[i * GRID_SIZE + j] != "." else 0
            for j in range(GRID_SIZE)
        ]
        for i in range(GRID_SIZE)
    ]
    print(grid)

    # Convert the grid to a string format that the solver can understand
    solver_grid = "".join(
        str(grid[i][j]) if grid[i][j] != 0 else "."
        for i in range(GRID_SIZE)
        for j in range(GRID_SIZE)
    )

    # Solve the Sudoku puzzle

    start = time.monotonic()
    solved_grid = solve(solver_grid)
    t = time.monotonic() - start
    print("Solved: %.5f sec" % t)

    # Convert the solved grid back to the format used by the GUI
    # Check if the puzzle was solved
    if solved_grid:
        # Convert the solved grid back to the format used by the GUI
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                grid[i][j] = int(solved_grid[squares[i * GRID_SIZE + j]])
    else:
        print("The Sudoku puzzle could not be solved.")
        return

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        window.fill(WHITE)

        draw_grid()
        draw_numbers(grid)

        pygame.display.update()


if __name__ == "__main__":
    main()

import time

import pygame
from arc_consistency import print_solution, solve

# Pygame constants
WINDOW_SIZE = 600


def draw_queen(screen, row, col, cell_size):
    pygame.draw.circle(
        screen,
        (255, 0, 0),
        (col * cell_size + cell_size // 2, row * cell_size + cell_size // 2),
        cell_size // 2 - 10,
    )


def draw_board(screen, n, cell_size):
    colors = [(255, 255, 255), (100, 100, 100)]  # Set two colors for chessboard pattern

    for row in range(n):
        for col in range(n):
            color = colors[((row + col) % 2)]
            pygame.draw.rect(
                screen, color, pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
            )


def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))

    # n = int(input("Enter the number of queens: "))
    n = 8
    if n < 1:
        print("Invalid input. Please enter a positive integer.")
        return

    cell_size = WINDOW_SIZE // n

    board = [[0] * n for _ in range(n)]
    start_time = time.monotonic()
    if solve(board, 0):
        print("Solution:")
        print_solution(board)
        print("Solved in %.6f seconds" % (time.monotonic() - start_time))

        draw_board(screen, n, cell_size)

        # Draw the solution using Pygame
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    draw_queen(screen, i, j, cell_size)
        pygame.display.flip()

        # Wait for the user to close the window
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
    else:
        print("No solution found.")


if __name__ == "__main__":
    main()

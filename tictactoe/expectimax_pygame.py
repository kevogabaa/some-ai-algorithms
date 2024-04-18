import pygame
from tictactoe_expectimax import TicTacToe

# Pygame settings
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 3, 3
SQUARE_SIZE = WIDTH // COLS

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Initialize Pygame and the display window
pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
FONT = pygame.font.Font(None, 40)  # Font to display the end game text


def draw_grid():
    for x in range(0, WIDTH, SQUARE_SIZE):
        pygame.draw.line(WIN, WHITE, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, SQUARE_SIZE):
        pygame.draw.line(WIN, WHITE, (0, y), (WIDTH, y))


def draw_board(board):
    for row in range(ROWS):
        for col in range(COLS):
            if board[row * ROWS + col] == "X":
                pygame.draw.circle(
                    WIN,
                    RED,
                    (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2),
                    SQUARE_SIZE // 3,
                )
            elif board[row * ROWS + col] == "O":
                pygame.draw.line(
                    WIN,
                    BLUE,
                    (col * SQUARE_SIZE, row * SQUARE_SIZE),
                    ((col + 1) * SQUARE_SIZE, (row + 1) * SQUARE_SIZE),
                    5,
                )
                pygame.draw.line(
                    WIN,
                    BLUE,
                    ((col + 1) * SQUARE_SIZE, row * SQUARE_SIZE),
                    (col * SQUARE_SIZE, (row + 1) * SQUARE_SIZE),
                    5,
                )


def draw_endgame_text(text):
    endgame_text = FONT.render(text, True, WHITE)
    WIN.blit(
        endgame_text,
        (WIDTH // 2 - endgame_text.get_width() // 2, HEIGHT // 2 - endgame_text.get_height() // 2),
    )


def main():
    clock = pygame.time.Clock()
    game = TicTacToe()
    run = True

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                col = x // SQUARE_SIZE
                row = y // SQUARE_SIZE
                move = row * ROWS + col
                if move in game.available_moves():
                    game.make_move(move, "X")
                    if not game.check_winner("X") and not game.num_empty_squares() == 0:
                        move = game.best_move("O", 10)
                        game.make_move(move, "O")

        draw_grid()
        draw_board(game.board)

        if game.check_winner("X"):
            draw_endgame_text("X wins!")
            pygame.display.update()
            pygame.time.wait(3000)  # Wait for 3 seconds before closing the game
            run = False
        elif game.check_winner("O"):
            draw_endgame_text("O wins!")
            pygame.display.update()
            pygame.time.wait(3000)  # Wait for 3 seconds before closing the game
            run = False
        elif game.num_empty_squares() == 0:
            draw_endgame_text("It's a tie!")
            pygame.display.update()
            pygame.time.wait(3000)  # Wait for 3 seconds before closing the game
            run = False

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()

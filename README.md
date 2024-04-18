# Sudoku and N-Queens Solver

This project contains Python scripts to solve Sudoku and N-Queens problems using various algorithms such as backtracking and arc consistency.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.x
- Pygame (for the GUI)
- NumPy

You can install requirements using pip:

```bash
pip install -r requirements.txt
```

## Sudoku, N-Queens, and Tic-Tac-Toe

### Sudoku Solver

The Sudoku problem is a classic example of a constraint satisfaction problem (CSP) in the field of Artificial Intelligence (AI).
A Sudoku puzzle is a 9x9 grid divided into nine 3x3 blocks, each containing nine cells.
The puzzle starts with some cells already filled with numbers from 1 to 9.
The objective is to fill the remaining cells such that each row, each column, and each 3x3 block contains all the numbers from 1 to 9 exactly once.

In terms of AI, each cell in the Sudoku grid can be seen as a variable, the numbers 1 to 9 as the domain of possible values, and the Sudoku rules as constraints that must be satisfied.
The problem is to find an assignment of values to variables that satisfies all constraints.

Solving a Sudoku puzzle involves `search and inference`.
Search is needed because there are many possible assignments of numbers to cells, and we need to find one that works.
Inference is used to update the domains of variables based on the constraints and the current assignment, which can help reduce the search space.

The Sudoku solver uses the `backtracking` algorithm to search for a solution to the puzzle.
Improved version of this solver uses `constraint propagation` techniques such as `arc consistency` to reduce the search space and speed up the solution process.
worth mentioning before going further is `Constraint propagation` is a technique used to reduce the domain of variables in a CSP by enforcing constraints between variables.
We use `constraint checking` to ensure that the constraints are satisfied and `constraint propagation` to update the domains of variables based on the constraints,
before going further to a more advanced technique, `arc consistency` is a constraint propagation technique that can be used to reduce the domain of variables in a CSP by removing values that are inconsistent with the constraints.

### N-Queens Solver

The N-Queens problem is another example of a CSP.
The problem is to place N queens on an N×N chessboard such that no two queens attack each other.
A queen can attack another queen if they are in the same row, column, or diagonal.

The N-Queens problem can be solved using `backtracking`, which is a general algorithm for finding all (or some) solutions to a computational problem.
The algorithm works by recursively trying all possible configurations of the queens on the board and backtracking when a conflict is detected.

Another approach to solving the N-Queens problem is to use `arc consistency`, which is a technique used to reduce the domain of variables in a CSP by removing values that are inconsistent with the constraints.
The arc consistency algorithm works by propagating constraints between variables to ensure that the constraints are satisfied.

Also, the N-Queens problem can be solved using `naked triples` technique, which is a constraint propagation technique that can be used to reduce the domain of variables in a CSP by identifying and removing values that are inconsistent with the constraints.
The naked triples algorithm works by identifying sets of three variables that have the same three possible values and removing those values from the other variables in the same row, column, or diagonal.

### Tic-Tac-Toe Solver

The Tic-Tac-Toe problem is a simple game where two players take turns placing their mark (X or O) on a 3x3 grid.
The first player to get three of their marks in a row (horizontally, vertically, or diagonally) wins the game.
The problem is to find the optimal move for a given board configuration.

The Tic-Tac-Toe solver uses the minimax algorithm with alpha-beta pruning to find the best move for the computer player.
The `minimax algorithm` is a decision-making algorithm that is used in two-player games to find the optimal move for the computer player assuming that the opponent plays perfectly.`
Alpha-beta pruning` is a technique used to reduce the number of nodes that need to be evaluated in the minimax algorithm by eliminating branches that are guaranteed to be worse than the current best move.

The `expectimax algorithm` is a variation of the minimax algorithm that is used in games where the opponent's moves are not deterministic.
In the expectimax algorithm, the opponent's moves are modeled as random events with probabilities, and the computer player makes decisions based on the expected value of the game outcome.

#!/usr/bin/python3
"""N Queens puzzle solver using backtracking."""

import sys


def print_usage_and_exit(message):
    """Prints error message and exits the program with status 1."""
    print(message)
    sys.exit(1)


def is_safe(queens, row, col):
    """
    Checks if placing a queen at (row, col) is safe.

    A queen placement is considered safe if it does not
    conflict with any other queen in the same column
    or on the diagonals.
    """
    for r, c in enumerate(queens):
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True


def solve_nqueens(N):
    """
    Solves the N queens problem for an NxN chessboard.

    Returns:
        List of all possible solutions, where each solution is a list
        of positions (row, column) of queens.
    """
    solutions = []

    def backtrack(queens):
        row = len(queens)
        if row == N:
            solutions.append([[r, c] for r, c in enumerate(queens)])
            return
        for col in range(N):
            if is_safe(queens, row, col):
                backtrack(queens + [col])

    backtrack([])
    return solutions


def main():
    """
    Main function to handle input validation and print solutions.

    Takes command-line argument N, validates it, and prints
    all solutions to the N queens problem.
    """
    if len(sys.argv) != 2:
        print_usage_and_exit("Usage: nqueens N")

    try:
        N = int(sys.argv[1])
    except ValueError:
        print_usage_and_exit("N must be a number")

    if N < 4:
        print_usage_and_exit("N must be at least 4")

    solutions = solve_nqueens(N)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()

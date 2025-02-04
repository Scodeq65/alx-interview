#!/usr/bin/python3
"""Module that determines the N queens solutions using backtracking."""

import sys


def print_usage_and_exit():
    """
    Prints the usage message and exits the program with status code 1.
    """
    print("Usage: nqueens N")
    sys.exit(1)


def validate_input():
    """
    Validates the command-line input to ensure that N is a valid integer
    greater than or equal to 4.
    """
    if len(sys.argv) != 2:
        print_usage_and_exit()

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    return n


def is_safe(queens, row, col):
    """
    Determines if a queen can be safely placed at the given row and column.
    """
    for r, c in enumerate(queens):
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True


def solve_n_queens(n):
    """
    Solves the N Queens problem for a given board size and prints each solution.
    """
    def backtrack(queens):
        """
        Recursively attempts to place queens row by row,
        printing solutions when found.
        """
        row = len(queens)
        if row == n:
            print([[r, c] for r, c in enumerate(queens)])
            return

        for col in range(n):
            if is_safe(queens, row, col):
                queens.append(col)  # Place queen
                backtrack(queens)   # Recurse to place next queen
                queens.pop()        # Remove queen (backtrack)

    backtrack([])


def main():
    """
    Main function to execute the N Queens program.
    """
    n = validate_input()
    solve_n_queens(n)


if __name__ == "__main__":
    main()

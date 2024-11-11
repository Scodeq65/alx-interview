#!/usr/bin/python3
"""N Queens puzzle solver using backtracking."""

import sys


def print_usage_and_exit():
    """
    Prints the usage message and exits the program with status code 1.
    Usage:
        nqueens N
    """
    print("Usage: nqueens N")
    sys.exit(1)


def validate_input():
    """
    Validates the command-line input to ensure that N is a valid integer
    greater than or equal to 4.

    If the input is invalid:
        - Prints an appropriate error message.
        - Exits the program with status code 1.

    Returns:
        int: The value of N if the input is valid.
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

    Args:
        queens (list): The current list of placed queens, where the index
                       represents the row, and the value at each index
                       represents the column of a queen.
        row (int): The row index to check for placing the queen.
        col (int): The column index to check for placing the queen.

    Returns:
        bool: True if the position is safe, False otherwise.
    """
    for r, c in enumerate(queens):
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True


def solve_n_queens(n):
    """
    Solves the N Queens problem for a given board size and prints
    each solution.

    Args:
        n (int): The size of the chessboard (N x N) and the number of
                 queens to place.

    Returns:
        list: A list containing all solutions, where each solution is a list of
              [row, column] pairs representing queen positions.
    """
    solutions = []

    def backtrack(queens):
        """
        Recursively attempts to place queens row by row,
        backtracking when necessary.

        Args:
            queens (list): Current list of queen positions up to
                           the current row.
        """
        row = len(queens)
        if row == n:
            solutions.append([[r, c] for r, c in enumerate(queens)])
            return
        for col in range(n):
            if is_safe(queens, row, col):
                queens.append(col)  # Place queen
                backtrack(queens)   # Recurse to place next queen
                queens.pop()        # Remove queen (backtrack)

    backtrack([])
    return solutions


def main():
    """
    Main function to execute the N Queens program.
    - Validates input.
    - Solves the N Queens problem.
    - Prints each solution in the required format.
    """
    n = validate_input()
    solutions = solve_n_queens(n)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()

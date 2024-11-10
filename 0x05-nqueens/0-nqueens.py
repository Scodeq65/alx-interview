#!/usr/bin/python3
"""N Queens puzzle"""
import sys


def print_usage_and_exit(message):
    print(message)
    sys.exit(1)


def is_safe(queens, row, col):
    """Check if placing a queen at (row, col) is safe."""
    for r, c in enumerate(queens):
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True


def solve_nqueens(N):
    """Recursive function to solve the N queens problem."""
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
    """Main function to handle input and print solutions."""
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

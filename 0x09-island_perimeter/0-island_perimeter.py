#!/usr/bin/python3
"""
Function to calculate the perimeter of an island described in a grid.
"""


def island_perimeter(grid):
    """
    Calculates the perimeter of the island in the given grid.

    Args:
        grid (list of list of int): 2D grid where 0
        represents water and 1 represents land.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:  # If it's a land cell
                # Check above
                if row == 0 or grid[row - 1][col] == 0:
                    perimeter += 1
                # Check below
                if row == len(grid) - 1 or grid[row + 1][col] == 0:
                    perimeter += 1
                # Check left
                if col == 0 or grid[row][col - 1] == 0:
                    perimeter += 1
                # Check right
                if col == len(grid[row]) - 1 or grid[row][col + 1] == 0:
                    perimeter += 1

    return perimeter

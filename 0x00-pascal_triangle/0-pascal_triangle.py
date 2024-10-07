#!/usr/bin/python3
"""
Module that contains the pascal_triangle function.
This function generates Pascal's triangle up to a given number of rows.
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers
    representing Pascal's Triangle up to n rows.

    Args:
        n (int): The number of rows to generate in Pascal's Triangle.

    Returns:
        list: A list of lists, where each inner list represents
        a row of Pascal's Triangle.
    """
    if n <= 0:
        return []

    """ The first row of Pascal's Triangle is always [1]
    """
    triangle = [[1]]

    for i in range(1, n):
        """ The first element of each row is always 1
        """
        row = [1]
        for j in range(1, i):
            """ Each element is the sum of the two elements directly above it
            """
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        """ The last element of each row is always 1
        """
        row.append(1)
        triangle.append(row)

    return triangle

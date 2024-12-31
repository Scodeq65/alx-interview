#!/usr/bin/python3
"""Rotate 2D Matrix"""


def rotate_2d_matrix(matrix):
    """
    Rotate an n x n 2D matrix 90 degrees clockwise in plac.

    Args:
        matrix (list[list[int]]): The 2D matrix to rotate.

    Returns:
        None: The matrix is modified in place.
    """
    n = len(matrix)

    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for i in range(n):
        start, end = 0, n - 1
        while start < end:
            matrix[i][start], matrix[i][end] = matrix[i][end], matrix[i][start]
            start += 1
            end -= 1

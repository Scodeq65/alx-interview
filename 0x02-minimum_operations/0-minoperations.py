#!/usr/bin/python3
"""
This module contains the minOperations function.

The function calculates the minimum number of
operations required
to result in exactly `n` 'H' characters in a file,
using only two
operations: Copy All and Paste.
"""


def minOperations(n):
    """
    Calculate the fewest number of operations needed
    to get exactly `n` H's.

    Parameters:
    n (int): The target number of H characters.

    Returns:
    int: The minimum number of operations, or 0 if impossible.
    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    # Loop until all factors are processed
    while n > 1:
        # Check if 'factor' divides 'n'
        while n % factor == 0:
            operations += factor  # Add the factor to operations
            n //= factor  # Reduce 'n' by dividing it by the factor
        factor += 1  # Move to the next possible factor

    return operations

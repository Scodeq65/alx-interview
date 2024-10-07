#!/usr/bin/phthon3
"""
Module that contains the Pascal_triangle function.
This func generate pascal's triangle uo to a given nos of rows.
"""


def pascal_triangle(n):
  """
  Returns a lists of int representing pascal's triangle

  Args:
    n (int): The nos of rows to generate in Pascal's Triangle.

  Returns:
    list: a list of lists, where each inner list represents a row of a Pascal's triangle
  """
  if n <= 0:
    return []

  """The first role of a pascal triangle is always [1]"""
  triangle = [[1]]

  for i in range(1, n):
    """the first element of each row is always 1"""
    row =[1]
    for j in range(1, i):
      """Each element is the sum of the two elements directly above it."""
      row.append(triangle[i - 1][j -1] + triangle[i -1][j])
    """The last element of each row is always 1"""
    row.append(1)
    triangle.append(row)

  return triangle
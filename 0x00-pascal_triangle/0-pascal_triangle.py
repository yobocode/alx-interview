#!/usr/bin/python3
"""A module containing Pascal's triangle.
"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing the Pascal's triangle.

    This function takes an integer argument n and returns a list of lists of
    integers representing the first n rows of Pascal's triangle.

    Args:
        n (int): The number of rows to generate.

    Returns:
        List[List[int]]: A list of lists of integers representing the first n
                         rows of Pascal's triangle.
    """
    if type(n) is not int or n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        row += [triangle[i-1][j-1] + triangle[i-1][j] for j in range(1, i)]
        row += [1]
        triangle.append(row)
    return triangle

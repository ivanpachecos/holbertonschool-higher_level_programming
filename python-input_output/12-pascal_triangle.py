#!/usr/bin/python3
"""
Create a function def pascal_triangle(n): that returns a list
of lists ofintegers representing the Pascal’s triangle of n:

Returns an empty list if n <= 0
You can assume n will be always an integer
You are not allowed to import any module
"""


def pascal_triangle(n):
    """
    Create a function
    """
    if n <= 0:
        return []

    triangle = [[1]]  # The first row is always [1]

    for i in range(1, n):
        row = [1]  # Every row starts with 1
        for j in range(1, i):
            # Each value is the sum of the two values above it
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  # Every row ends with 1
        triangle.append(row)

    return triangle

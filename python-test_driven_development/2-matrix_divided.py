#!/usr/bin/python3

"""
This module contains a function to divide all elements of a
matrix by a divisor.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor and rounds the result
    to 2 decimal places.

    Args:
        matrix (list): A matrix (list of lists) of integers or floats.
        div (int/float): The divisor by which to divide the elements of
                         the matrix.

    Raises:
        TypeError: If the matrix is not a list of lists of integers/floats.
        TypeError: If any element of the matrix is not an integer or float.
        TypeError: If the rows of the matrix do not have the same size.
        TypeError: If div is not a number (integer or float).
        ZeroDivisionError: If div is zero.

    Returns:
        list: A new matrix with the results of the division, rounded to 2
              decimal places.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list)
                                               for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(isinstance(number, (int, float)) for row in matrix
               for number in row):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [
        [round(number / div, 2) for number in row]
        for row in matrix
    ]

    return new_matrix

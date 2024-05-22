#!/usr/bin/python3

def matrix_divided(matrix, div):

    """
        Divides all elements of a matrix by a divisor and rounds the result
        to 2 decimal places.

    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(isinstance(number, (int, float)) for row in matrix for number in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(number / div, 2) for number in row] for row in matrix]
    
    return new_matrix
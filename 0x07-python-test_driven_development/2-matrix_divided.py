#!/usr/bin/python3
"""
This module defines one function; 'matrix_divided()'.
It takes a matrix with equal rows, and a diving number as input
--------
It returns the matrix with each element divided by the dividing number
"""


def matrix_divided(matrix, div):
    """Takes a matrix with equal rows, and a dividing number
        to divide each element in the matrix.
    """

    new_matrix = []

    if not isinstance(matrix, list) or len(matrix) == 0 or \
        not isinstance(matrix[0], list) or len(matrix[0]) == 0:
        raise TypeError("""matrix must be a matrix (list of lists)
                of integers/floats""")

    matrix_length = len(matrix[0])

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for mat in matrix:
        if len(mat) != matrix_length or not isinstance(mat, list):
            raise TypeError("Each row of the matrix must have the same size")
        inter_list = []
        for element in mat:
            if type(element) not in [int, float]:
                raise TypeError("""matrix must be a matrix (list of lists)
                        of integers/floats""")
            inter_list.append(round(element / div, 2))
        new_matrix.append(inter_list)

    return new_matrix

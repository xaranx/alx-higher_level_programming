#!/usr/bin/python3


def matrix_divided(matrix, div):
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError ("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError ("matrix must be a matrix (list of lists) of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError ("Each row of the matrix must have the same size")
        for item in row:
            if not isinstance(item, int) and not isinstance(item, float):
                raise TypeError ("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError ("div must be a number")
    if div == 0:
        raise ZeroDivisionError ("division by zero")
    return[[round(item / div, 2) for item in row] for row in matrix]

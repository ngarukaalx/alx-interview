#!/usr/bin/python3
"""Rotate 2D matrix"""


def rotate_2d_matrix(matrix):
    """performs 2D matrix rotate
    it 90 degrees clockwise
    """
    n = len(matrix)
    # loop through cycles
    for i in range(n // 2):
        # loop through items in rows
        for j in range(i, n - 1 - i):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n - 1 - j][i]
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
            matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
            matrix[j][n - 1 - i] = temp

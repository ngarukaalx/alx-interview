#!/usr/bin/python3
"""
returns a list of lists of integers representing the Pascal’s
triangle of n
"""


def pascal_triangle(n):
    """function to return a list of list of intergers rep pascall
    args: n - size of triangle
    assumes n is always an interger
    """
    tringle = []

    # return empty list if n is 0 or less than 0
    if n <= 0:
        return tringle
    for i in range(n):
        row = [1]
        # skip the first and last element
        for j in range(1, i):
            row.append(tringle[i-1][j-1] + tringle[i-1][j])
        if i > 0:
            # append 1 at end of each row
            row.append(1)

        # append each row
        tringle.append(row)
    return tringle

#!/usr/bin/python3
"""This module contains fuction that gets the
perimeter of an highland
"""


def island_perimeter(grid):
    """returns the perimeter of the island described in a grid
    grid is a list of list of intergers
    """
    if grid is None:
        return

    num_rows = len(grid)
    num_cols = len(grid[0])

    # initialize perimeter to zero
    perimeter = 0

    # iterate through rows:
    for i in range(num_rows):
        # iterate through elements
        for j in range(num_cols):
            current_element = grid[i][j]

            # check if the current element is 1 rep land
            if current_element == 1:
                # check left
                if j > 0:
                    # check prev element is 0 means water
                    if grid[i][j - 1] == 0:
                        perimeter += 1
                # check top
                if i > 0:
                    # check if top element is 0
                    if grid[i - 1][j] == 0:
                        perimeter += 1
                # check right
                if j < num_cols - 1:
                    # check if is zero
                    if grid[i][j + 1] == 0:
                        perimeter += 1
                # check bottom
                if i < num_rows - 1:
                    # check if the bottom of current element is zero
                    if grid[i + 1][j] == 0:
                        perimeter += 1
    return perimeter

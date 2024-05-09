#!/usr/bin/python3
"""This module contains island perimeter function"""


def island_perimeter(grid):
    """Returns the perimeter of the island described in a grid."""
    num_rows = len(grid)
    num_cols = len(grid[0])

    perimeter = 0

    for i in range(num_rows):
        for j in range(num_cols):
            if grid[i][j] == 1:
                perimeter += 4

                # Check left neighbor
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 1

                # Check top neighbor
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 1

                # Check right neighbor
                if j < num_cols - 1 and grid[i][j + 1] == 1:
                    perimeter -= 1

                # Check bottom neighbor
                if i < num_rows - 1 and grid[i + 1][j] == 1:
                    perimeter -= 1

    return perimeter

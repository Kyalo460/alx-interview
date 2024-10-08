#!/usr/bin/python3
"""Returns the perimeter of the island described in grid."""


def island_perimeter(grid):
    """Returns the perimeter or 0 if the island doesn't exist."""
    perimeter = 0

    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            sides = 4
            if grid[i][j] == 1:
                # check previous grid
                if grid[i][j - 1]:
                    if grid[i][j - 1] == 1:
                        sides -= 1
                        
                # check grid above
                if grid[i - 1]:
                    if grid[i - 1][j] == 1:
                        sides -= 1

                # check next grid
                if grid[i][j + 1]:
                    if grid[i][j + 1] == 1:
                        sides -= 1

                # check grid below
                if grid[i + 1]:
                    if grid[i + 1][j] == 1:
                        sides -= 1

                # add sides to perimeter
                perimeter += sides

    return perimeter    
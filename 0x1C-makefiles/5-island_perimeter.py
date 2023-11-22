#!/usr/bin/python3
"""Island perimeter function defined"""


def island_perimeter(grid):
    """Return the island perimeter
    The grid shows water by 0 and land by 1
    Args:
        grid (list): A list of list of integers representing an island.
    Returns:
        Island perimeter
    """
    width = len(grid[0])
    height = len(grid)
    border = 0
    size = 0

    for i in range(height):
        for j in range(width):
            if grid[i][j] == 1:
                size += 1
                if (j > 0 and grid[i][j - 1] == 1):
                    border += 1
                if (i > 0 and grid[i - 1][j] == 1):
                    border += 1
    return size * 4 - border * 2

#!/usr/bin/python3
"""A function that defines a Pascal's triangle"""


def pascal_triangle(n):
    """Represent a Pascal's triangle of size n

    Returns:
        A list of lists of integers representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        Ptriangle = triangles[-1]
        tempTriangle = [1]
        for i in range(len(Ptriangle) - 1):
            tempTriangle.append(Ptriangle[i] + Ptriangle[i + 1])
        tempTriangle.append(1)
        triangles.append(tempTriangle)
    return triangles

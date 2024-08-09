#!/usr/bin/python3
"""Returns a pascal's triangle inform of a matrix."""


def pascal_triangle(n):
    """Returns a matrix if n > 0."""
    arr = []

    if n <= 0:
        return arr

    for i in range(n):
        inner_arr = []
        for j in range(i+1):
            if i == 0:
                inner_arr.append(1)
            elif j == 0:
                inner_arr.append(1)
            elif j == i:
                inner_arr.append(1)
            else:
                num = arr[i - 1][j - 1] + arr[i - 1][j]
                inner_arr.append(num)

        arr.append(inner_arr)

    return arr

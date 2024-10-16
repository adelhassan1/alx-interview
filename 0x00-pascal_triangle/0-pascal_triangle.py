#!/usr/bin/python3
"""
Pascal triangle
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal's triangle of n
    """
    result = [[1]]

    if n <= 0:
        return []

    for i in range(n - 1):
        temp = [0] + result[-1] + [0]
        row = []
        for j in range(len(result[-1]) + 1):
            row.append(temp[j] + temp[j + 1])
        result.append(row)
    return result

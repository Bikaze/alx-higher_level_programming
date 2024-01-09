#!/usr/bin/python3
"""
pascal_triangle(n)
"""


def pascal_triangle(n):
    """Display pascal's triangle for until length 'n'"""

    if n <= 0:
        return []
    if n == 1:
        return [[1]]

    sub_level = pascal_triangle(n - 1)
    lower_level = sub_level[-1]
    new_level = []

    for i in range(len(lower_level) + 1):
        if i == 0 or i == len(lower_level):
            new_level.append(1)
        else:
            new_level.append(lower_level[i] + lower_level[i - 1])
    sub_level.append(new_level)
    return sub_level

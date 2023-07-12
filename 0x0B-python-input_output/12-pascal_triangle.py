#!/usr/bin/python3

def pascal_triangle(n):
    """Returns the Pascal's triangle up to the given number of lines.

    Args:
        n (int): Number of lines in the Pascal's triangle.

    Returns:
        list: A matrix representing the Pascal's triangle.
    """

    matrix = []
    prev_row = []

    for i in range(n):
        row = []
        prev = -1
        nxt = 0
        for j in range(len(prev_row) + 1):
            if prev == -1 or nxt == len(prev_row):
                row.append(1)
            else:
                row.append(prev_row[prev] + prev_row[nxt])
            prev += 1
            nxt += 1
        matrix.append(row)
        prev_row = row[:]

    return matrix

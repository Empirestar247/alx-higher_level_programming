#!/usr/bin/python3
"""Defines an integer addition function."""


def add_integer(a, b=98):
    """Return the integer addition of a and b.

    Arguments:
        a (int, float): First number.
        b (int, float): Second number (default is 98).

    Returns:
        int: Integer addition of a and b.

    Raises:
        TypeError: If either a or b is a non-integer and non-float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")
    return int(a) + int(b)

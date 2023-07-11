#!/usr/bin/python3
"""Check if an object is an instance of a specific class."""


def is_same_class(obj, a_class):
    """Check if obj is an exact instance of a_class."""
    if type(obj) is a_class:
        return True
    return False

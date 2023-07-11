#!/usr/bin/python3
"""
Return a list of available attributes and methods of an object.
"""


def lookup(obj):
    """
    Return a list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        A list of attribute and method names.
    """
    return dir(obj)


# Example usage
my_object = [1, 2, 3]
result = lookup(my_object)
print(result)

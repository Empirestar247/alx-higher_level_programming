#!/usr/bin/python3
"""
    8-class_to_json: class_to_json()
"""


def class_to_json(obj):
    """
    Returns the dictionary description of an object of a simple data structure.

    Args:
        obj: The object to convert to a dictionary.

    Returns:
        dict: The dictionary representation of the object.
    """
    return obj.__dict__

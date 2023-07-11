#!/usr/bin/python3
"""
Module to load an object from a JSON file.
"""


import json


def load_from_json_file(filename):
    """
    Load an object from a JSON file.

    Args:
        filename (str): Name of the file.

    Returns:
        object: The loaded object.
    """
    with open(filename, "r") as json_file:
        my_obj = json.load(json_file)
        return my_obj

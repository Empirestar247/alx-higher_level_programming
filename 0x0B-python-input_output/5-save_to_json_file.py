#!/usr/bin/python3
"""
Module to save an object to a JSON file.
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Write an object to a JSON file.

    Args:
        my_obj (object): Object to be serialized.
        filename (str): Name of the file where the JSON string is stored.
    """
    with open(filename, "w") as json_file:
        json.dump(my_obj, json_file)

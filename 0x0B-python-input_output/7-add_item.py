#!/usr/bin/python3
"""
This script adds all arguments to a Python List and saves the List to a file.
"""

import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file


if __name__ == "__main__":
    filename = "add_item.json"

    try:
        arg_list = load_from_json_file(filename)
    except FileNotFoundError:
        arg_list = []

    for arg in sys.argv[1:]:
        arg_list.append(arg)
    save_to_json_file(arg_list, filename)

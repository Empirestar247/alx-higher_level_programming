#!/usr/bin/python3
"""
Module with a method named inherits_from
"""


def inherits_from(obj, a_class):
    """
    Returns True if an object is an instance of a class that inherited from;
    otherwise, returns False.
    """
    return False if type(obj) is a_class else isinstance(obj, a_class)

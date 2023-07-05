#!/usr/bin/python3
"""Defines a locked class that restricts attribute creation."""


class LockedClass:
    """
    Prevent the user from instantiating new LockedClass attributes
    for anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]

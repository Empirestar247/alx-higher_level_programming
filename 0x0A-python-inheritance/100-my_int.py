#!/usr/bin/python3
"""
Module that contains the definition of the MyInt class
"""


class MyInt(int):
    """Definition of the MyInt class that inherits from the int class"""

    def __eq__(self, other):
        """Overrides the equals operator, inverting it"""
        return int(self) != int(other)

    def __ne__(self, other):
        """Overrides the not-equals operator, inverting it"""
        return int(self) == int(other)

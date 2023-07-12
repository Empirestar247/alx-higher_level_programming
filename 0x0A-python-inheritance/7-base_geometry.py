#!/usr/bin/python3
"""
Module with the BaseGeometry class
"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Method for calculating the area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method for validating if a number is an integer"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

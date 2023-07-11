#!/usr/bin/python3

"""
Module with class BaseGeometry
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle, which inherits BaseGeometry
    """

    def __init__(self, size):
        """
        Method to initialize the attributes
        """

        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Method to calculate the area of the square
        """

        return self.__size ** 2

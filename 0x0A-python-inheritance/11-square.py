#!/usr/bin/python3

"""
Module with class BaseGeometry
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle
    """

    def __init__(self, size):
        """
        Method to initialize the attributes
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Method to calculate the area of the square
        """
        return self.__size ** 2

    def __str__(self):
        """
        __str__ method to return a string representation of the square
        """
        return "[Square] {}/{}".format(self.__size, self.__size)

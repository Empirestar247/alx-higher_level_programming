#!/usr/bin/python3

"""
Module with the Square class
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle,
    which inherits from BaseGeometry
    """

    def __init__(self, size):
        """Method for initializing the attributes"""

        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Method for calculating the area of the square"""

        return self.__size ** 2

#!/usr/bin/python3

"""
Module with the Square class
"""

from 9-rectangle import Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle
    """

    def __init__(self, size):
        """
        Initializes the Square object.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__width * self.__height

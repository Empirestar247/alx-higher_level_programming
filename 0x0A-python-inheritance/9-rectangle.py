#!/usr/bin/python3

"""
Module with class BaseGeometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """
        Method to initialize the attributes
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Method to calculate the area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        __str__ method to return a string representation of the rectangle
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

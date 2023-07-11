#!/usr/bin/python3
"""
    10-student: class Student
"""


class Student:
    """
    A class that defines a student.

    Attributes:
        first_name (str): First name of the student.
        last_name (str): Last name of the student.
        age (int): Age of the student.

    Methods:
        __init__ - Initializes the Student instance.
        to_json - Retrieves a dictionary representation of Student instance.
        reload_from_json - Replaces all attributes of the Student instance.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance.

        Args:
            first_name (str): First name of the student.
            last_name (str): Last name of the student.
            age (int): Age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        """
        Retrieves a dictionary representation of the Student instance.

        Args:
            attr (list): Attribute names to be retrieved.

        Returns:
            dict: Dictionary representation of the Student instance.
        """
        if attr is not None:
            res = {k: self.__dict__[k] for k in self.__dict__.keys() & attr}
            return res
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance.

        Args:
            json (dict): Dictionary containing the attribute data.
        """
        for key, value in json.items():
            self.__setattr__(key, value)

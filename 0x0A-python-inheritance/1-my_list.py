#!/usr/bin/python3
"""Define the MyList class that inherits from the list class."""


class MyList(list):
    """A custom list class that inherits from the built-in list class."""

    def print_sorted(self):
        """Print the list in sorted (ascending) order."""

        # Create a copy of the list to avoid modifying the original list
        copy_list = self.copy()

        # Sort the copied list in ascending order
        copy_list.sort()

        # Print the sorted list
        print("{}".format(copy_list))

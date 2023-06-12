#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """
    Prints the elements of a list as integers, each on a new line.

    Args:
        my_list (list): The list of integers to be printed. Defaults to an empty list if not provided.

    Returns:
        None
    """
    if my_list:
        # Use a list comprehension to convert each element to a string and join them with newlines
        print('\n'.join(['{:d}'.format(n) for n in my_list]))

# Example usage
my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)

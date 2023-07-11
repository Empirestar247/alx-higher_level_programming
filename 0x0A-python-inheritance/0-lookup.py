def lookup(obj):
    """
    Return the list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        A list of attribute and method names.
    """
    return [name for name in dir(obj) if not name.startswith('__')]


# Example usage
my_list = [1, 2, 3]
result = lookup(my_list)
print(result)

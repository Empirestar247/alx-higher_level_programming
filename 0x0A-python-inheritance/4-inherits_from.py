def is_kind_of_class(obj, a_class):
    """
    Define if obj is an instance of a_class or its subclasses.
    Returns True if obj is an instance of a_class or its subclasses,
    False otherwise.
    """
    # Check if obj is an instance of a_class or its subclasses
    if isinstance(obj, a_class):
        return True

    # Check if obj is an instance of any subclasses of a_class
    for subclass in a_class.__subclasses__():
        if isinstance(obj, subclass):
            return True

    return False

#!/usr/bin/python3

if __name__ == "__main__":
    """Print all names defined by hidden_4 module."""

    # Import the hidden_4 module
    import hidden_4

    # Get all the names defined in the module
    module_names = dir(hidden_4)

    # Iterate through each name
    for name in module_names:
        # Check if the name does not start with "__"
        if not name.startswith("__"):
            # Print the name
            print(name)

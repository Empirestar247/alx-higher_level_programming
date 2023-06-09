#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    # Get the count of arguments (excluding the script name)
    count = len(sys.argv) - 1

    # Check the number of arguments and print the appropriate message
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))

    # Iterate through each argument and print its position and value
    for i in range(count):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))

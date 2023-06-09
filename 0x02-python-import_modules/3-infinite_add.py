#!/usr/bin/python3
import sys

if __name__ == "__main__":
    # Get the number of arguments
    num_args = len(sys.argv) - 1

    # Print the number of arguments
    if num_args == 0:
        print("Number of argument(s): 0.")
    elif num_args == 1:
        print("Number of argument(s): 1 (argument):")
    else:
        print("Number of argument(s): {} (arguments):".format(num_args))

    # Print the list of arguments
    for i, arg in enumerate(sys.argv[1:], start=1):
        print("{}: {}".format(i, arg))

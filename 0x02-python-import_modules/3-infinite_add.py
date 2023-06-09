#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    # Get the number of arguments
    num_args = len(sys.argv) - 1

    # Print the number of arguments
    if num_args == 0:
        print("Number of argument(s): 0.")
    elif num_args == 1:
        print("Number of argument(s): 1.")
    else:
        print("Number of argument(s):", num_args, ".")

    # Print the list of arguments
    if num_args > 0:
        print("Arguments:")
        for i, arg in enumerate(sys.argv[1:], start=1):
            print(i, ":", arg)

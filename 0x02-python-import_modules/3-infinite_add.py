#!/usr/bin/python3

if __name__ == "__main__":
    """Print the addition of all arguments."""
    import sys

    total = 0
    # Iterate through each argument except the first one
    for i in range(len(sys.argv) - 1):
        # Convert the argument to an integer and add it to the total
        total += int(sys.argv[i + 1])

    # Print the total
    print("{}".format(total))

#!/usr/bin/python3
"""Defines a function to print a text with new lines after specific characters."""


def text_indentation(text):
    """Prints the text with new lines after characters '.', '?', and ':'.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0

    # Skip leading whitespace
    while i < len(text) and text[i] == ' ':
        i += 1

    # Iterate through the text
    while i < len(text):
        print(text[i], end="")

        # Check for newline or specific characters
        if text[i] == "\n" or text[i] in ".?:":
            if text[i] in ".?:":
                print("\n")
            i += 1

            # Skip consecutive whitespace
            while i < len(text) and text[i] == ' ':
                i += 1

            continue

        i += 1

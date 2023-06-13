#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy = my_list.copy()  # Copy original list.
    for x in my_list:
        if idx == my_list.index(x):  # Replace element at index.
            copy[idx] = element
            return copy  # Return updated list.
        elif idx >= len(my_list):  # Return list if index out of range.
            return copy
        elif idx < 0:  # Return list if index is negative.
            return copy

#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    for x in my_list:
        if idx == my_list.index(x):  # Find the element at the specified index.
            my_list.pop(idx)  # Remove the element at the index.
            my_list.insert(idx, element)  # Insert the new element at the index.
            return my_list  # Return the updated list.
        elif idx >= len(my_list):  # If index is out of range, return the original list.
            return my_list
        elif idx < 0:  # If index is negative, return the original list.
            return my_list

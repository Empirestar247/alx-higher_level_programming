#!/usr/bin/python3
def element_at(my_list, idx):
    for x in my_list:
        if idx == my_list.index(x):  # Find element at specified index.
            return(x)  # Return the element.
        elif idx > len(my_list):  # If index is out of range, return None.
            return None
        elif idx < 0:  # If index is negative, return None.
            return None

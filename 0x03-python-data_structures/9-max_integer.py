#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None  # Empty list case
    max_num = my_list[0]  # Assume the first element is the maximum
    for num in my_list:
        if num > max_num:
            max_num = num  # Update maximum if a larger number is found
    return max_num

#!/usr/bin/python3
def no_c(my_string):
    l = list(my_string)
    for x in l:
        if x == 'c':  # Remove lowercase 'c'.
            l.remove('c')
        if x == 'C':  # Remove uppercase 'C'.
            l.remove('C')
    my_string = "".join(l)
    return my_string

#!/usr/bin/python3
'''
Function that inserts a line of text to a file,
after each line containing a specific string
'''


def append_after(filename="", search_string="", new_string=""):
    '''
    Function to insert a line after each occurrence of a specific string
    in a file

    Args:
        filename (str): Name of the file
        search_string (str): String to search for
        new_string (str): Line of text to insert
    '''
    updated_content = ''
    with open(filename) as file:
        for line in file:
            updated_content += line
            if search_string in line:
                updated_content += new_string
    with open(filename, 'w') as file:
        file.write(updated_content)

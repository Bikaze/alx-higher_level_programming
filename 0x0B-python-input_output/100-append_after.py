#!/usr/bin/python
"""
append_after() function
"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file, after each line containing
    a specific string
    """

    with open(filename, 'r') as f:
        data = f.readlines()

    for i in range(len(data)):
        if search_string in data[i]:
            data.insert(i+1, new_string)

    with open(filename, 'w') as f:
        f.writelines(data)

#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = dict(a_dictionary)
    for k in list(new):
        new[k] *= 2
    return new

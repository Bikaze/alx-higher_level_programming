#!/usr/bin/python3
def new_in_list(mylist, idx, element):
    my_list = [x for x in mylist]
    if idx >= 0:
        if idx < len(my_list):
            my_list[idx] = element
            return my_list
        else:
            return my_list
    else:
        return my_list

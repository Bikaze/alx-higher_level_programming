#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    box = []
    if len(my_list) > 0:
        for i in my_list:
            if i % 2 == 0:
                box.append(True)
            else:
                box.append(False)
        return box

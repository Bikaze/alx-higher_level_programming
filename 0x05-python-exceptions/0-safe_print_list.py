#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            i += 1
        print()
    except (RuntimeError, IndexError):
        print()
        return (i)
    else:
        return (i)

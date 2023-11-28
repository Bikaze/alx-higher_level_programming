#!/usr/bin/python3
for i in range(97, 123):
    if i == ord('q') or i == ord('e'):
        pass
    else:
        print("{:c}".format(i), end="")

#!/usr/bin/python3
def uppercase(word):
    for c in word:
        if ord(c) >= 97 and ord(c) <= 123:
            new = ord(c) - 32
        else:
            new = ord(c)
        print("{:c}".format(new), end="")
    print()

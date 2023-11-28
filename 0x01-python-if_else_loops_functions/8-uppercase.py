#!/usr/bin/python3
def uppercase(word):
    for c in word:
        if ord(c) >= 97 and ord(c) <= 123:
            print("{:c}".format(ord(c) - 32), end="")
        else:
            print("{:c}".format(ord(c)), end="")

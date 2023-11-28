#!/usr/bin/python3
def uppercase(word):
    new = ""
    for c in word:
        if ord(c) >= 97 and ord(c) <= 123:
            new += chr(ord(c) - 32)
        else:
            new += c
    return new

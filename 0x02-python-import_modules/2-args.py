#!/usr/bin/python3
import sys
argv = sys.argv
length = len(argv) - 1
i = 1
if length == 0:
    print("0 arguments.")
elif length == 1:
    print("1 argument:")
else:
    print(f"{length} arguments:")
while i <= length:
    print(f"{i}: {argv[i]}")
    i += 1

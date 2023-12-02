#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for mat in matrix:
        for elem in mat:
            if elem == mat[-1]:
                print("{:d}".format(elem), end="")
            else:
                print("{:d}".format(elem), end=" ")
        print()

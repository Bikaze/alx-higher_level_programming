#!/usr/bin/python3
"""This algorithm finds a peak in a list of unsorted numbers"""


def find_peak(list_int):
    """This function takes a list of numbers and returns one peak"""
    if len(set(list_int)) == 1:
        return list_int[0]
    for i in range(len(list_int)):
        if not list_int[i-1] or list_int[i] > list_int[i-1]:
            if not list_int[i+1] or list_int[i] > list_int[i+1]:
                return list_int[i]
                break

#!/usr/bin/python3
"""This algorithm finds a peak in a list of unsorted numbers"""


def find_peak(list_int):
    """This function takes a list of numbers and returns one peak"""
    if len(list_int) == 0:
        return None
    if len(list_int) == 1:
        return list_int[0]

    i = len(list_int) // 2
    if not list_int[i-1] or list_int[i] > list_int[i-1]:
        if not list_int[i+1] or list_int[i] > list_int[i+1]:
            return list_int[i]
        return find_peak(list_int[i+1:])
    return find_peak(list_int[:i])

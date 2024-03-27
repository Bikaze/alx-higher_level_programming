#!/usr/bin/python3
"""This algorithm finds a peak in a list of unsorted numbers"""


def find_peak(list_int):
    """This function takes a list of numbers and returns one peak"""
    left, right = 0, len(list_int) - 1

    while left <= right:
        m = (left + right) // 2
        
        if m > 0 and list_int[m] < list_int[m-1]:
            right = m - 1
        elif m < len(list_int) - 1 and list_int[m] < list_int[m + 1]:
            left = m + 1
        else:
            return list_int[m]

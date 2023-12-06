#!/usr/bin/python3
def best_score(a_dictionary):
    if (a_dictionary) is None:
        return None
    else:
        new = list(a_dictionary)
        maxi = new[0]
        for i in new:
            if a_dictionary[i] > a_dictionary[maxi]:
                maxi = i
        return maxi

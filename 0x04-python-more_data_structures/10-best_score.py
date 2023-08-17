#!/usr/bin/python3

def best_score(a):
    if len(a) == 0:
        return None
    k = list(a.keys())[0]
    big = a[k]
    for key, value in a.items():
        if value > big:
            big = value
            k = key
    return k

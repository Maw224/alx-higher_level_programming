#!/usr/bin/python3

def complex_delete(a, val):
    while val in a.values():
        for k, v in a.items():
            if v == value:
                del a[k]
                break
    return a

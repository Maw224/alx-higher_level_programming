#!/usr/bin/python3

def simple_delete(a, k=""):
    if k in a:
        del a[k]
    return a

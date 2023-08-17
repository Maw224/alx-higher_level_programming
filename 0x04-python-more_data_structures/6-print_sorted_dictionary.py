#!/usr/bin/python3

def print_sorted_dictionary(a):
    for i in sorted(a):
        print("{}: {}".format(i, a[i]))

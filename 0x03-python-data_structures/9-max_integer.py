#!/usr/bin/python3

def max_integer(my_list):
    x = 0
    for i in my_list:
        x = i if i > x
    return x

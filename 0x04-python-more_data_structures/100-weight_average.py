#!/usr/bin/python3

def weight_average(my_l=[]):
    if not isinstance(my_l, list) or len(my_l) == 0:
        return 0
    av = 0
    s = 0
    for x in my_l:
        av += x[0] * x[1]
        s += x[1]
    return av/s

#!/usr/bin/python3

def weight_average(my_l=[]):
    av = 0
    s = 0
    for x in my_l:
        av += x[0] * x[1]
        s += x[1]
    return av/s

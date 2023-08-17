#!/usr/bin/python3
def multiply_list_map(l):
    return ([map(lambda(x: x * 2), x) for x in l])

#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    new = []
    for i in range(len(my_list)):
        new[i] = my_list[i] % 2 == 0
    return new

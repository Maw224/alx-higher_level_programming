#!/usr/bin/python3

def new_in_list(my_list, idx, el):
    copy = [x for x in my_list]
    if idx >= 0 and idx < len(my_list):
        copy[idx] = el
    return (copy)

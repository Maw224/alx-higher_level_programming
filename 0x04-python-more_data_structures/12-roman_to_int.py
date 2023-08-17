#!/usr/bin/python3

def roman_to_int(rs):
    if not isinstance(rs, str) or len(rs) == 0:
        return 0
    rd = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    n = 0

    for i in range(len(rs)):
        if i != len(rs) - 1 and rd[rs[i]] < rd[rs[i + 1]]:
            n += rd[rs[i]] * -1
        else:
            n += rd[rs[i]]
    return n

#!/usr/bin/python3

if __name__ == "__main":
    import sys

    _sum = 0
    count = len(sys.argv) - 1

    for i in range(count):
        _sum += int(sys.argv[i+1])
    print("{}".format(_sum))

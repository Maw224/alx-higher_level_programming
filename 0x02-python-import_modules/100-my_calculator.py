#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import *
    import sys

    if len(sys.argv) - 1 != 3:
        print ("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    operation = sys.argv[2]
    b = int(sys.argv[3])
    operations = {"+": add, "-": sub, "*": mul, "/": div}

    if operation not in list(operations.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    
    print("{} {} {} = {}".format(a, operation, b, operations[operation](a, b)))

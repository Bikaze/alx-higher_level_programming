#!/usr/bin/python3
import calculator_1 as calc
if __name__ == '__main__':
    a = 10
    b = 5
    add = calc.add
    div = calc.div
    sub = calc.sub
    mul = calc.mul
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} + {} = {}".format(a, b, sub(a, b)))
    print("{} + {} = {}".format(a, b, mul(a, b)))
    print("{} + {} = {}".format(a, b, div(a, b)))

import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt
import time
from math import *

global iterator
iterator = 0

def diff2(f, x, er):
    global iterator
    r = (f(x - er) - 2 * f(x) + f(x + er)) / (er * er)
    iterator += 1
    return r


def trapezint(f, a, b, n):
    global iterator
    h = (b - a) / n
    iterator += 1
    sum = 0
    part1 = (0.5) * h * (f(a) + f(b))
    iterator += 1
    for i in range(1, n):
        xi = a + i * h
        iterator += 1
        sum = sum + f(xi)
        iterator += 1
    return part1 + h * sum


def adaptive(f, a, b, ep, numSteps):
    global iterator
    max = 0
    step = float(abs(a - b) / numSteps)
    iterator += 1
    i = 0
    while (i < numSteps):
        iterator += 1
        i = i + 1
        adj = a
        adj = a + step * i
        iterator += 1
        dval = diff2(f, adj, ep)
        if (abs(dval) > max):
            iterator += 1
            max = abs(dval)

    h = sqrt(12 * ep) * ((b - a) * max) ** .5
    iterator += 1
    n = (b - a) / h
    iterator += 1
    estimated = trapezint(f, a, b, int(ceil(n)))
    estimated = eval(str(estimated))
    print("The estimated value after " + str(numSteps) + " steps is " + str(round(estimated,8)))
    iterator += 1
    actual = quad(f,a,b)
    actual = eval(str(actual))
    print("The actual value is " + str(round(actual[0]+actual[1],8)))
    iterator += 1
    error = abs(actual[0]-estimated)
    iterator += 1
    print("Adaptive error: " + str(round(error,8)))
    print("Number of Iterations: " + str(iterator))
    value = trapezint(f, a, b, int(ceil(n)))
    iterator = 0
    return value


# def main():
#     func =
#     a = 0
#     b = 1
#     ep = 0.5E-09
#     #print trapezint(func, a, b, 10)
# adaptive(lambda x: ln(x**2+1), 0, 1, 0.5E-09, 1000)




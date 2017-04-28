from __future__ import division
from sympy import *
import re


def printDerivative(expr, derivative):
    expression = str(expr).strip('exp')[:-1][1:]
    print('Input function: ' + expression)
    expression = re.escape(expression)
    string = str(derivative)
    regex = '\*?exp\(' + expression + '\)\*?'
    string = re.sub(regex, '', string)
    string = string.strip('*')
    print('Derivative: ' + string)


def autoDiff(func, variables):
    variable_count = len(variables.split(' '))

    if variable_count == 0:
        print('Error: You must pass at least one variable.')
    if variable_count == 1:
        x = symbols(variables)
        expr = exp(func(x))
        printDerivative(expr, (diff(expr, x)))

    elif variable_count == 2:
        x, y = symbols(variables)
        expr = exp(func(x, y))
        printDerivative(expr, (diff(expr, x, y)))

    elif variable_count == 3:
        x, y, z = symbols(variables)
        expr = exp(func(x, y, z))
        printDerivative(expr, (diff(expr, x, y, z)))

    else:
        print('More than 3 variables are not supported.')


if __name__ == '__main__':
    autoDiff(lambda x: 2*x**2, 'x')
    autoDiff(lambda x, y: 2*x**2 + 4*y**3, 'x y')
    autoDiff(lambda x, y, z: 2 * x ** 2 + 4 * y ** 3 + 8 * z ** 4, 'x y z')

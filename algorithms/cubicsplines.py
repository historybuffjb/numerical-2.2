import numpy as np
import re
import matplotlib.pyplot as plt

debug = False


# Takes a string of points in the string form: '(-1,3), (0,5), (3,1), (4,1), (5,1)'
# and optionally, the graph resolution.
# Prints the cubic spline functions to stdout and displays an interpolated line plot
# Example usage: cubicSpline('(-1,3), (0,5), (3,1), (4,1), (5,1)')
# or cubicSpline('(-1,3), (0,5), (3,1), (4,1), (5,1)', resolution=2) for a low resolution graph.

def cubicSpline(points, resolution=100):
    if not points:
        raise Exception('You must provide in data points.')
        return

    # Parse the coordinate inputs
    if not points.count('(') == points.count(')'):
        raise Exception('Input coordinates were malformed.')
        return

    coordinates = re.findall(r'\(.*?\)', points)

    coordinates = [item.replace('(', '').replace(')', '') for item in coordinates]

    # Split and convert values
    x = []
    y = []
    for coordinate in coordinates:
        try:
            x_val, y_val = [float(num) for num in coordinate.split(',')]
            x.append(x_val)
            y.append(y_val)
        except ValueError:
            raise Exception('Input coordinates were malformed.')

    if not len(x) == len(y):
        raise Exception('Length of X and Y arrays must be equal.')
        exit(1)

    # Sort the input, just in case
    y = [y for (x, y) in sorted(zip(x, y))]
    x.sort()

    # Get the number of inputs
    n = len(x)

    # Solve for little delta
    delta = np.zeros((n - 1, 1))
    for i in range(0, n - 1):
        delta[i] = x[i + 1] - x[i]

    # Solve for big delta
    Delta = np.zeros((n - 1, 1))
    for i in range(0, n - 1):
        Delta[i] = y[i + 1] - y[i]

    if debug:
        print(delta)
        print(Delta)

    A = np.zeros((n, n))

    A[0, 0] = 1
    A[n - 1, n - 1] = 1

    for i in range(1, n - 1):
        A[i, i - 1] = delta[i - 1]
        A[i, i] = 2 * (delta[i - 1] + delta[i])
        A[i, i + 1] = delta[i]

    b = np.zeros((n, 1))

    for i in range(1, n - 1):
        b[i] = (3 * ((Delta[i] / delta[i]) - (Delta[i - 1] / delta[i - 1])))

    # Solve for c coefficients
    ci = np.linalg.solve(A, b)

    if debug:
        print(ci)

    # Solve for d coefficients
    di = np.zeros((n - 1, 1))
    for i in range(0, n - 1):
        di[i] = (ci[i + 1] - ci[i]) / (3 * delta[i])

    if debug:
        print(di)

    # Solve for b coefficients
    bi = np.zeros((n - 1, 1))
    for i in range(0, n - 1):
        bi[i] = (Delta[i] / delta[i]) - (delta[i] / 3) * (2 * ci[i] + ci[i + 1])

    # And finally, let's get our formulas!
    Si = []
    formulas = []
    for i in range(0, n - 1):
        tempFormula = "{0} + {1}* (x_val - {2}) + {3}* (x_val - {4})**2 + {5}* (x_val - {6})**3"
        tempFormula = tempFormula.format(str(y[i]), str(bi[i]), str(x[i]), str(ci[i]), str(x[i]), str(di[i]), str(x[i]))

        # ugly but formats the formula nice
        tempFormula = re.sub(' +', ' ', tempFormula.replace('[', ' ').replace(']', ' '))
        tempString = (("S{0}(x) = " + tempFormula).format(str(i + 1)).replace('**', '^')
                      .replace('x_val', 'x').replace('- -', '+ ').replace('x - 0', 'x'))
        formulas.append(tempFormula)
        Si.append(tempString)

    for i in range(0, len(Si)):
        print(Si[i])

    x_vals = []
    y_vals = []
    # Set up the plot
    for i in range(0, n - 1):
        xf = np.linspace(x[i], x[i + 1], resolution)
        yf = []

        for j in range(0, resolution):
            # Due to Python's variable declarations we have x_val references in the formulas,
            # but PEP 8 will complain the value is unused. It's not.
            x_val = xf[j]
            yf.append(eval(formulas[i]))

        x_vals.extend(xf)
        y_vals.extend(yf)

    plt.plot(x, y, 'o', x_vals, y_vals, '-')

    plt.legend(['Input X Values', 'Cubic Spline curve'], loc='best')
    plt.title('Cubic Spline Interpolation')
    # plt.show()

#cubicSpline('(0,1),(2,2),(3,4)')


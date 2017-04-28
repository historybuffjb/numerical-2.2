import matplotlib
matplotlib.use("TkAgg")

import tkinter as tk
import timeit
import io
import sys
import traceback
import math
from math import sqrt
from sympy import ln
from algorithms.chebyshev import chebyshev
from algorithms.cubicsplines import cubicSpline
from algorithms.leastSquares import leastSquares
from algorithms.bezier import bezier
from algorithms.nonlinearleastsquares import nonLinearLeastSquares
from algorithms.differencemethods import differenceMethods
from algorithms.extrapolation import extrapolation
from algorithms.autodiff import autoDiff
from algorithms.trapezoidalsimpson import newtTrapSimp
from algorithms.romberg1 import romberg
from algorithms.adaptive import adaptive
from algorithms.gaussian import gaussian
from algorithms.trapezoidalsimpson import newtonTrapezoidal
from algorithms.trapezoidalsimpson import newtonSimpson
from numpy import sin, cos, tan, log

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

categories = ['Chebyshev', 'Cubic Splines', 'Bezier', 'Linear Least Squares', 'Nonlinear Least Squares',
              'Difference Methods', 'Extrapolation', 'Automatic Differentiation', 'Newton-Cotes', 'Romberg', 'Adaptive', 'Gaussian']


def callback(tex, input):
    plt.clf()
    out = io.StringIO()
    sys.stdout = out
    tex.delete("1.0",tk.END)
    try:
        w=input.get()
        start = timeit.default_timer()
        exec(w)
        stop = timeit.default_timer()
        fig.canvas.draw()
        sys.stdout = sys.__stdout__
        tex.insert(tk.END, out.getvalue())
        tex.insert(tk.END, 'Runtime: ' + str(stop - start) + ' seconds')
        tex.see(tk.END)  # Scroll if necessary
    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        tex.insert(tk.END, str(e))
        tex.insert(tk.END, str(traceback.extract_tb(exc_traceback)))
        tex.insert(tk.END, "You have entered an invalid input. Select a function from the left for example input.\n")

root = tk.Tk()
root.wm_title('Numerical Analysis Project 2.2')
right = tk.Frame()
right.pack(side=tk.RIGHT, expand=1, fill=tk.BOTH)

# hack
tex = tk.Text()

inputframe = tk.Frame(right)
inputframe.pack(side=tk.TOP, padx=(0,8), pady=(8,8), fill=tk.X)
inputlabel = tk.Label(inputframe, text='Input: ')
inputlabel.pack(side=tk.LEFT, padx=(0,4))

inputText = tk.StringVar()


def setInput(tex, category):
    tex.delete("1.0", tk.END)
    plt.clf()
    if category == 'Chebyshev':
        inputText.set('chebyshev(-1, 1, 0.5, math.sin)')
        tex.insert(tk.END,  'chebyshev(a [Number], b [Number], x [Number], f [Function])\n'
                            'a, b = interval [a,b]; x = x value of function to approximate; f = function to approximate\n\n'
                            'Runs the Chebyshev algorithm up to 30 times, increasing degree n until the guess is '
                            'sufficiently close. Outputs the calculated Chebyshev value, the degree of the polynomial '
                            'where the best guess was calculated and the actual value from the function.\n\n'
                            'Example usage: chebyshev(-1, 1, 0.5, math.sin)\n'
                            'Advanced functions can be input as example: lambda x: (math.sin(x) - math.cos(x))')
    elif category == 'Cubic Splines':
        inputText.set('cubicSpline(\'(-1,3), (0,5), (3,1), (4,1), (5,1)\')')
        tex.insert(tk.END,  'cubicSpline(points [String], resolution [Integer - Default 100])\n'
                            'points = string of coordinate points; resolution affects how smooth the plot is\n\n'
                            'Prints the cubic spline functions and displays an interpolated line plot below.\n'
                            'Example usage: cubicSpline(\'(-1,3), (0,5), (3,1), (4,1), (5,1)\')\n'
                            'or cubicSpline(\'(-1,3), (0,5), (3,1), (4,1), (5,1)\', resolution=2) for a ' 
                            'low resolution graph.')
    elif category == 'Bezier':
        inputText.set('bezier([[1,0,6,2],[1,-1,0,1],[1,1,6,0]])')
        tex.insert(tk.END,  'bezier(points [Array])\n'
                            'points = Series of points in the form: [[1,0,6,2],[1,-1,0,1],[1,1,6,0]]\n\n'
                            'Outputs the Bezier spline\'s knots and control points based on the input coordinates.\n'
                            'Example usage: bezier([[1,0,6,2],[1,-1,0,1],[1,1,6,0]])')
    elif category == 'Linear Least Squares':
        inputText.set('leastSquares([(1.49, 44.6), (3.03, 57.8), (0.57, 49.9), (5.74, 61.3), (3.51, 49.6), '
                      '(3.73, 61.8), (2.98, 49.0), (-0.18, 44.7), (6.23, 59.2), (3.38, 53.9), (2.15, 46.5), '
                      '(2.10, 54.7), (3.93, 50.3), (2.47, 51.2), (-0.41, 45.7)],0,2)')
        tex.insert(tk.END,  'leastSquares(points [Array])\n'
                            'leastSquares(points [Array], n [Integer])\n'
                            'points = Series of points in the form: [[0, 1], [1, 2], [2, 3]] or [(0, 1), (1, 2), (2, 3)]\n'
                            'n = degree (only used when points are provided using parentheses\n\n'
                            'Takes either a series of coordinate points or a series of A and B matrices in bracket form.'
                            'If coordinates are provided, will output least squares fit function and graph.\n'
                            'If an A and B matrix is provided, it will output the coefficient, residual, and rank.\n\n'
                            'Example usage: leastSquares([[1, 1], [1, -1], [1, 1]], [2, 1, 3], 3)')
    elif category == 'Nonlinear Least Squares':
        inputText.set('Not yet implemented')
        tex.insert(tk.END, ''
                           ''
                           ''
                           '')
    elif category == 'Difference Methods':
        inputText.set('Not yet implemented')
        tex.insert(tk.END, ''
                           ''
                           ''
                           '')
    elif category == 'Extrapolation':
        inputText.set('extrapolation(lambda x: -sin(x),0,2,0.01)')
        tex.insert(tk.END, 'extrapolation(f [Function], xval [Number], n [Number], hval [Number])\n'
                           'f = function to approximate; xval = value to extrapolate from; n = levels of of extrapolation; hval = step size\n\n'
                            'Takes in a function in terms of x along with the xval you wish to eval f\'(xval) at\n.'
                           'You must provide the value for n, which is the number of levels of extrapolation, and \n'
                           'you must provide the initial stepsize h. This will return the most accurate value for \n'
                            'f\'(xval) along with the actual value and the error. You MUST enter a single variable function\n'
                           'Example usage: extrapolation(lambda x: -sin(x),0,2,0.01)')
    elif category == 'Automatic Differentiation':
        inputText.set('autoDiff(lambda x: x**2, \'x\')')
        tex.insert(tk.END, 'autoDiff(f [Function])\n'
                           'f = function to differentiate\n\n'
                           'Takes a function and calculates the derivative via automatic differentiation.\n'
                           'Functions can be input as Pythonic lambda functions or basic sin/cos/tan et cetera.\n'
                           'Supports up to three variables (x, y, z) in space-delimited string form: \'x y z\'\n\n'
                           'Example usage: autoDiff(lambda x: x**2, \'x\')'
                           '\nautoDiff(lambda x, y, z: 2 * x ** 2 + 4 * y ** 3 + 8 * z ** 4, \'x y z\')')
    elif category == 'Newton-Cotes':
        inputText.set('newtTrapSimp(lambda x: x**2, 0, 1, 10)')
        tex.insert(tk.END, 'newtTrapSimp(f [Function], a [Number], b[Number], n[Number])\n'
                           'f = function to approximate; a, b = interval [a,b]; n = # of steps to take\n\n'
                           'Calculates the best guess for the Newton-Cotes Trapezoidal/Newton-Cotes Simpson result value, and plots the '
                           'graph below.\n\n'
                           'Example usage: newtTrapSimp(lambda x: x**2, 0, 1, 10)')
    elif category == 'Romberg':
        inputText.set('romberg(math.sin, 0, 2, 10)')
        tex.insert(tk.END, 'romberg(f [Function], a [Number], b[Number], n[Number])\n'
                           'f = function to approximate; a, b = interval [a,b]; n = # of steps to take\n\n'
                           'Plots the Romberg output and also outputs the associated array.\n\n'
                           'Example usage: romberg(math.sin, 0, 2, 10)\n'
                           'Advanced functions can be input as example: lambda x: (math.sin(x) - math.cos(x))')
    elif category == 'Adaptive':
        inputText.set('adaptive(lambda x: ln(x**2+1), 0, 1, 0.5E-09, 100)')
        tex.insert(tk.END,  'adaptive(f [Function], a [Number], tolerance[Number], steps[Number])\n'
                            'a, b = interval [a,b]; tolerance = guess tolerance; steps = # of steps to take\n\n'
                            'Takes a function, a - b interval, tolerance, and number of steps and outputs the integrated'
                            ' function value, the adaptive error, and the number of iterations necessary to find the '
                            'integrated value. \n'
                            'Example usage: adaptive(lambda x: ln(x**2+1), 0, 1, 0.5E-09, 100)')
    elif category == 'Gaussian':
        inputText.set('gaussian(lambda x: (x**2 * log(x)), 1, 3)')
        tex.insert(tk.END,  'gaussian(f [Function], a [Number], b[Number], y[Number - Default None])\n'
                            'a, b = interval [a,b]; f = function to approximate; y = Gaussian Y value\n\n'
                            'Takes a function, a and b interval, and optionally, an extra Y value.'
                            'Outputs the estimated value, the actual value, and the error.\n'
                            'Example usage: gaussian(lambda x: (x**2 * log(x)), 1, 3)')
    else:
        print('Error')

userinput = tk.Entry(inputframe, textvariable=inputText)
userinput.pack(side=tk.LEFT, fill=tk.X, expand=1, padx=(4,4))

fig = plt.figure(1)
canvas = FigureCanvasTkAgg(fig, master=right)
plt.ion()
plot_widget = canvas.get_tk_widget()
plot_widget.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)

txt_frm = tk.Frame(right)
txt_frm.pack(side=tk.RIGHT, fill="x", expand=True)
# ensure a consistent GUI size
txt_frm.grid_propagate(False)
# implement stretchability
txt_frm.grid_rowconfigure(0, weight=1)
txt_frm.grid_columnconfigure(0, weight=1)

tex = tk.Text(txt_frm, height=12)
tex.pack(fill='x')

executebutton = tk.Button(inputframe, text='Execute', command=lambda: callback(tex, userinput))
executebutton.pack(side=tk.RIGHT, padx=(4, 0))


def close():
    root.destroy()
    exit(0)

bop = tk.Frame(width=200)
bop.pack(side=tk.LEFT, fill='y', pady=(8, 8), padx=(8, 8))
for k in range(0, 12):
    tv = categories[k]
    b = tk.Button(bop, text=tv, command=lambda tv=tv: setInput(tex, tv))
    b.pack(fill="x", pady=(2, 2))
tk.Button(bop, text='Exit', command=lambda: close()).pack(side=tk.BOTTOM, fill='x')

# UI hacks
root.protocol("WM_DELETE_WINDOW", close)
root.lift()

root.attributes('-topmost', True)
root.after_idle(root.attributes, '-topmost', False)

def main():
    inputText.set("Select a button from the left for example input.")
    while True:
        try:
            root.mainloop()
            break
        # More hacks
        except UnicodeDecodeError:
            pass
        except KeyboardInterrupt:
            close()

if __name__ == '__main__':
    main()

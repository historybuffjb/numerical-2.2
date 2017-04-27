import matplotlib
matplotlib.use("TkAgg")

import tkinter as tk
import timeit
import io
import sys
import traceback
import math
from chebyshev import chebyshev
from cubicsplines import cubicSpline
from leastSquares import leastSquares
from bezier import bezier
from nonlinearleastsquares import nonLinearLeastSquares
from differencemethods import differenceMethods
from extrapolation import extrapolation
from autodiff import autoDiff
from trapezoidalsimpson import newtonTrapezoidal
from trapezoidalsimpson import newtonSimpson
from romberg1 import romberg
from adaptive import adaptive
from gaussian import gaussian
from numpy import sin, cos, tan, log

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

categories = ['Chebyshev', 'Cubic Splines', 'Bezier', 'Linear Least Squares', 'Nonlinear Least Squares',
              'Difference Methods', 'Extrapolation', 'Automatic Differentiation', 'Newton-Cotes: Trapezoidal',
            'Newton-Cotes: Simpson', 'Romberg', 'Adaptive', 'Gaussian']


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
        tex.insert(tk.END, 'Runtime: ' + str(stop - start) + 'ms')
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
inputframe.pack(side=tk.TOP, padx=(0,8), pady=(8,8), fill=tk.X, expand=1)
inputlabel = tk.Label(inputframe, text='Input: ')
inputlabel.pack(side=tk.LEFT, padx=(0,4))

inputText = tk.StringVar()


def setInput(tex, category):
    tex.delete("1.0", tk.END)
    plt.clf()
    if category == 'Chebyshev':
        inputText.set('chebyshev(-1, 1, 0.5, math.sin)')
        tex.insert(tk.END,  'Runs the Chebyshev algorithm up to 30 times, increasing degree n until the guess is'
                            'sufficiently close. Outputs the calculated Chebyshev value, the degree of the polynomial '
                            'where the best guess was calculated and the actual value from the function.\n\n'
                            'Example usage: chebyshev(-1, 1, 0.5, math.sin)\n'
                            'Advanced functions can be input as example: lambda x: (math.sin(x) - math.cos(x))')
    elif category == 'Cubic Splines':
        inputText.set('cubicSpline(\'(-1,3), (0,5), (3,1), (4,1), (5,1)\')')
        tex.insert(tk.END,  'Takes a string of points in the string form: \'(-1,3), (0,5), (3,1), (4,1), (5,1)\'' 
                            ' and optionally, the graph resolution.'
                            'Prints the cubic spline functions and displays an interpolated line plot below.\n'
                            'Example usage: cubicSpline(\'(-1,3), (0,5), (3,1), (4,1), (5,1)\')\n'
                            'or cubicSpline(\'(-1,3), (0,5), (3,1), (4,1), (5,1)\', resolution=2) for a ' 
                            'low resolution graph.')
    elif category == 'Bezier':
        inputText.set('bezier([[1,0,6,2],[1,-1,0,1],[1,1,6,0]])')
        tex.insert(tk.END,  'Takes a series of points in the form: [[1,0,6,2],[1,-1,0,1],[1,1,6,0]] and outputs the '
                            'Bezier spline\'s knots and control points based on the input coordinates.\n'
                            'Example usage: bezier([[1,0,6,2],[1,-1,0,1],[1,1,6,0]])')
    elif category == 'Linear Least Squares':
        inputText.set('leastSquares([(1.49, 44.6), (3.03, 57.8), (0.57, 49.9), (5.74, 61.3), (3.51, 49.6), '
                      '(3.73, 61.8), (2.98, 49.0), (-0.18, 44.7), (6.23, 59.2), (3.38, 53.9), (2.15, 46.5), '
                      '(2.10, 54.7), (3.93, 50.3), (2.47, 51.2), (-0.41, 45.7)],0,2)')
        tex.insert(tk.END, 'Takes either a series of coordinate points or a series of A and B matrices in bracket form.'
                           'If coordinates are provided, will output least squares fit function and graph.\n'
                           'If an A and B matrix is provided, it will output the coefficient, residual, and rank.'
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
        inputText.set('Not yet implemented')
        tex.insert(tk.END, ''
                           ''
                           ''
                           '')
    elif category == 'Automatic Differentiation':
        inputText.set('Not yet implemented')
        tex.insert(tk.END, ''
                           ''
                           ''
                           '')
    elif category == 'Newton-Cotes: Trapezoidal':
        inputText.set('Not yet implemented')
        tex.insert(tk.END, ''
                           ''
                           ''
                           '')
    elif category == 'Newton-Cotes: Simpson':
        inputText.set('Not yet implemented')
        tex.insert(tk.END, ''
                           ''
                           ''
                           '')
    elif category == 'Romberg':
        inputText.set('romberg(math.sin, 0, 2, 10)')
        tex.insert(tk.END, 'Takes a function, a, b, and n value in that order. Plots the Romberg output and also'
                           ' outputs the associated array.\n\n'
                           'Example usage: romberg(math.sin, 0, 2, 10)\n'
                           'Advanced functions can be input as example: lambda x: (math.sin(x) - math.cos(x))')
    elif category == 'Adaptive':
        inputText.set('Not yet implemented')
        tex.insert(tk.END, ''
                           ''
                           ''
                           '')
    elif category == 'Gaussian':
        inputText.set('gaussian(lambda x: (x**2 * log(x)), 1, 3)')
        tex.insert(tk.END, 'Takes a function, a and b interval, and optionally, an extra Y value.'
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
plot_widget.pack(side=tk.BOTTOM, fill=tk.BOTH)

txt_frm = tk.Frame(right)
txt_frm.pack(side=tk.RIGHT, fill="x", expand=True)
# ensure a consistent GUI size
txt_frm.grid_propagate(False)
# implement stretchability
txt_frm.grid_rowconfigure(0, weight=1)
txt_frm.grid_columnconfigure(0, weight=1)

tex = tk.Text(txt_frm, height=10)
tex.pack(fill='x', padx=(0,16))

executebutton = tk.Button(inputframe, text='Execute', command=lambda: callback(tex, userinput))
executebutton.pack(side=tk.RIGHT, padx=(4, 0))

bop = tk.Frame(width=200)
bop.pack(side=tk.LEFT, fill='y', pady=(8, 8), padx=(8, 8))
for k in range(0, 13):
    tv = categories[k]
    b = tk.Button(bop, text=tv, command=lambda tv=tv: setInput(tex, tv))
    b.pack(fill="x", pady=(2, 2))
tk.Button(bop, text='Exit', command=root.destroy).pack(side=tk.BOTTOM, fill='x')


def main():
    inputText.set("Select a button from the left for example input.")
    while True:
        try:
            root.mainloop()
            break
        except UnicodeDecodeError:
            pass

if __name__ == '__main__':
    main()

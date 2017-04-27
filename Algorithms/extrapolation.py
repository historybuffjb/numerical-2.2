import numpy as np
from sympy import *
import matplotlib.pyplot as plt
import time


def extrapolation(func,x, n, h):
	funch = eval(str(func))
	h = h /2
	funch2 = eval(str(func))

	return (2**n *funch2 - funch)/ (2**n -1)

def plot(result):
	plt.plot(result,'k--',label= "Extrapolation")

	legend = plt.legend(loc='upper center', shadow=True)
	frame = legend.get_frame()
	plt.show()

def main():
	x = Symbol('x')
	h = Symbol('h')
	hval = [0.1, 0.01,0.001]
	xval = 1
	func = sin(x+h)
	result = []
	n = 2
	start = time.time()
	for item in hval :
		result.append(extrapolation(func, xval, n, item))
	end = time.time()
	timeElapsed = end-start
	print ("Elapsed time: %f" % timeElapsed)
	plot(result)


if __name__ == "__main__":
	main()
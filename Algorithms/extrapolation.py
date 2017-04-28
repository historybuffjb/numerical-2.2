import numpy as np
from sympy import *
from scipy.misc import derivative
import matplotlib.pyplot as plt
import time


def extrapolationEvaluate(func,x, n, h):
	d = np.array( [[0] * (n + 1)] * (n + 1), float )

	for i in range( n + 1 ):
		d[i,0] = 0.5 * ( func( x + h ) - func( x - h ) ) / h

		powerOf4 = 1  # values of 4^j
		for j in range( 1, i + 1 ):
			powerOf4 = 4 * powerOf4
			d[i,j] = d[i,j-1] + ( d[i,j-1] - d[i-1,j-1] ) / ( powerOf4 - 1 )

		h = 0.5 * h

	return d

def plot(result):
	plt.plot(result,'k--',label= "Extrapolation")
	legend = plt.legend(loc='upper center', shadow=True)
	frame = legend.get_frame()

def extrapolation(func, xval, n, hval):
	result = []
	result = extrapolationEvaluate(func, xval, n, hval)
	print("The closest approximation is: " + str(result[n][n]))
	deriv = derivative(func, xval, dx=1e-6, n=1)
	print("The actual value is " + str(round(deriv,8)))
	print("This gives an error of: " + str(round(deriv-result[n][n], 8)))
	plot(result)
	return 0
#
# def main():
# 	hval = 0.01
# 	xval = 0
# 	n = 2
# 	func =lambda x: -sin(x)
# 	extrapolation(lambda x: -sin(x),0,2,0.01)
#
#
# if __name__ == "__main__":
# 	main()
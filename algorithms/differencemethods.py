import numpy as np
from sympy import *
import matplotlib.pyplot as plt
import time

def actual_result(func, val):
	x = Symbol('x')
	dfunc = diff(func, 'x')
	x = val
	return eval(str(dfunc))

def two_point(func, x, h):
	funcx = eval(str(func))
	x = x+h
	funcxh = eval(str(func))
	return (funcxh - funcx)/h

def three_point(func, x, h):
	x = x+h
	funcxh = eval(str(func))
	x = x-2*h
	funcxmh = eval(str(func))
	return (funcxh - funcxmh)/(2*h)

def plot(Result2Point,Result3Point,Error2Point,Error3Point):
	plt.plot(Result2Point, 'k--',label= "2 Point")
	plt.plot(Result3Point,'k:',label= "3 Point")
	plt.plot(Error2Point,'k',label= "2 Point Error")
	plt.plot(Error3Point,'k',label= "3 Point Error")

	legend = plt.legend(loc='upper center', shadow=True)
	frame = legend.get_frame()
	frame.set_facecolor('0.90')



def differenceMethods(func, x, h):
	Result2Point= []
	Result3Point= []
	Error2Point = []
	Error3Point = []
	actualResult = actual_result(func, x)
	for item in h:
		Result2Point.append(two_point(func, x, item))
		Result3Point.append(three_point(func, x, item))
	print("The closest 2point point is: " + str(round(Result2Point[-1], 8)))
	print("The closest 3point point is: " + str(round(Result3Point[-1], 8)))
	Error2Point = np.asarray(Result2Point) - actualResult
	Error3Point = np.asarray(Result3Point) - actualResult
	print("The error in the closest 2point is: " + str(round(Error2Point[-1], 8)))
	print("The error in the closest 3point is: " + str(round(Error3Point[-1], 8)))
	plot(Result2Point, Result3Point, Error2Point, Error3Point)
	return 0

# def main():
# 	differenceMethods('1/x', 2, [0.1,0.01,0.001])
# 	#
# 	# start = time.time()
# 	# actualResult = actual_result(func, xval)
# 	# for item in h:
# 	# 	Result2Point.append(two_point(func, xval, item))
# 	# 	Result3Point.append(three_point(func, xval, item))
# 	#
# 	# Error2Point = np.asarray(Result2Point) - actualResult
# 	# Error3Point = np.asarray(Result3Point) - actualResult
# 	#
# 	# end = time.time()
# 	# timeElapsed = end-start
# 	# print ("Elapsed time: %f" % timeElapsed)
# 	#
# 	#
# 	# plot(Result2Point, Result3Point, Error2Point, Error3Point)
#
#
# 	#print actual_result(func, xval)
#
# if __name__ =='__main__':
# 	main()

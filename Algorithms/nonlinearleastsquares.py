from scipy.optimize import *
from scipy.linalg import *
import numpy as np
from lmfit import *
import matplotlib.pyplot as plt

def gaussNewton(c, radii, initial):
    try:
        # Initialize variables
        A = []
        r = []
        vk = []
        x = initial
        # Loop through until end
        for i in range(len(c)):
            A = jacob(c, x)
            r = rFunc(c, radii, x)
            vk = np.linalg.solve(np.matmul(np.transpose(A),A),np.matmul(-np.transpose(A), r))
            x = x + vk
        print("The final values are: " + str((np.round(x,8))))
        err = np.sum(np.array(r)**2)
        print("The error value is: " + str(round(err,8)))
        RMSE = np.sqrt(err)/np.sqrt(len(c))
        print("The RMSE error is: "+ str(round(RMSE, 8)))
        return x
    except:
        print("I'm sorry, you have entered an invalid input!")
        return -1

def rFunc(c, radii, initial):
    r = []
    for i in range(len(c)):
        x = initial[0]-c[i][0]
        y = initial[1]-c[i][1]
        r.append(np.sqrt(x**2+y**2)-radii[i])
    return r


def jacob(c, initial, *func):
    A = []
    s = []
    for i in range(len(c)):
        s.append(np.sqrt(((initial[0]-c[i][0])**2)+((initial[1]-c[i][1])**2)))
        topX = initial[0]-c[i][0]
        topY = initial[1]-c[i][1]
        A.append([topX/s[i], topY/s[i]])
    return A

def levenMarquardt(func, c,initial,lamd):
    try:
        x = initial
        # Loop through until end
        x = least_squares(func, initial, '3-point', method='lm')

        print("The final values are: " + str(x))
        return x
    except Exception as e:
        print(e)
        print("I'm sorry, you have entered an invalid input!")
        return -1

gaussNewton([[-1,0],[1,1/2],[1,-1/2]],[1,1/2,1/2],[0,0], )
levenMarquardt(lambda x,y, z, w, t: x*np.exp(y(t))*np.cos(z+w), [[1,3],[2,5],[2,7],[3,5],[4,1]],[1,1,1],50)
def nonLinearLeastSquares(func,params):

    return 0

#
# def main():
#     func = lambda x: y=
#     x = np.array([0, 1, 0])
#     y = np.array([1, 1, -1])
#     r = np.array([1, 1, 1])
#     gauss_newton(x,y,r, [0,0])
#
#
# if __name__ == '__main__':
#   main()
#
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.optimize import curve_fit
#
# def func(x, a, b, c):
#     return a * np.exp(-b * x) + c
#
#
# xdata = np.linspace(0, 4, 50)
# y = func(xdata, 2.5, 1.3, 0.5)
# y_noise = 0.2 * np.random.normal(size=xdata.size)
# ydata = y + y_noise
# plt.plot(xdata, ydata, 'b-', label='data')
#
# popt, pcov = curve_fit(func, xdata, ydata)
# print(popt)
# print(pcov)
# plt.plot(xdata, func(xdata, *popt), 'r-', label='fit')
#
#
# popt, pcov = curve_fit(func, xdata, ydata, bounds=(0, [3., 2., 1.]))
# plt.plot(xdata, func(xdata, *popt), 'g--', label='fit-with-bounds')
#
# plt.xlabel('x')
# plt.ylabel('y')
# plt.legend()
# plt.show()
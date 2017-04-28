from scipy.optimize import *
from scipy.linalg import *
from sympy import *
import numpy as np
import matplotlib.pyplot as plt



# be aware that this will only do
# gauss-newton with circles and radii
# due to technical limitations we were unable
# to implement Levenberg Marquardt and so
# it is not included with this project
def nonLinearLeastSquares(c, radii, initial):
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
        e = sys.exc_info()[0]
        write_to_page("<p>Error: %s</p>" % e)
        print("I'm sorry, you have entered an invalid input!")
        return -1

def rFunc(c, radii, initial):
    r = []
    for i in range(len(c)):
        x = initial[0]-c[i][0]
        y = initial[1]-c[i][1]
        r.append(np.sqrt(x**2+y**2)-radii[i])
    return r



def jacob(c, initial):
    A = []
    s = []
    for i in range(len(c)):
        s.append(np.sqrt(((initial[0]-c[i][0])**2)+((initial[1]-c[i][1])**2)))
        topX = initial[0]-c[i][0]
        topY = initial[1]-c[i][1]
        A.append([topX/s[i], topY/s[i]])
    return A



#nonLinearLeastSquares([[-1,0],[1,1/2],[1,-1/2]],[1,1/2,1/2],[0,0])



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

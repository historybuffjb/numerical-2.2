from scipy.optimize import *
from scipy.linalg import *
import numpy as np
import matplotlib.pyplot as plt


def gauss_newton(x, y, r, p0):
  length = len(x)
  initial = np.array(p0)
  x_solve = [length]
  y_solve = [length]
  vk = [length]
  x_solve[0] = p0[0]
  y_solve[0] = p0[0]
  vk[0] = p0[0]
  for i in range(length):
    A = fsolve(x_solve[i], p0)
    vk[i] =  np.solve(-np.transpose(A)*np.sqrt((p0[0]-x_solve[i])**2+(p0[1]-y_solve[i])**2), np.transpose(A)*A)
    x_solve[i+1] = x_solve[i] + vk[i]
  print(x_solve[length])

def nonLinearLeastSquares(x,y,z):
    return 0

#
# def main():
#     x = np.array([0, 1, 0])
#     y = np.array([1, 1, -1])
#     r = np.array([1, 1, 1])
#     gauss_newton(x,y,r, [0,0])
#
#
# if __name__ == '__main__':
#   main()


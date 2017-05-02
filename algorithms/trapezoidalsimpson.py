from sympy import *
import matplotlib.pyplot as plt
from scipy.misc import derivative
import scipy.integrate as integrate

global iteration
iteration = 0

# This function calculates the Compositie Trapezoidal rule
# Function must be continuous along a and b. The value n
# is going to be the number of steps you want to use to calculate
# the rule
def newtonTrapezoidal(f,a,b,n):
    global iteration
    # create an array to store the plot data
    array = []
    # get your midpoint
    h=(b-a)/n
    # initializse the sum
    trapezoidalSum=0
    # first calculate step 1
    part1=(0.5)*h*(f(a)+f(b))
    # keep doing this n times
    for i in range(1,n):
        # compute your xi
        xi=a+i*h
        # add f evaluated at xi to sum
        trapezoidalSum=trapezoidalSum+f(xi)
        #add new estimate to array
        array.append(part1+h*trapezoidalSum)
        iteration += 1
    # now that you have all necesarry data go ahead and plot array
    plt.plot(array, 'k--', label="Trapezoidal")
    plt.legend(loc='best')

    print('Trapezoidal result: ' + str(round(part1+h*trapezoidalSum,8)))
    # last midpoint to check...
    h = (b - a) / n
    # get the derivative for the error at last a,b
    c = derivative(f, float(a + b) / 2, n=2)
    # computer error
    error = round((((b - a) ** 2) * (h ** 2) * c) / 25,8)
    # output error
    print('Trapezoidal error: ' + str(error))
    print("Trapezoidal Iteration Count: " + str(iteration))

global iteration2
iteration2 = 0
# this function does the same as trapezoidal,
# except it uses the Simpson composite rule
def newtonSimpson(f, a, b, n):
    global iteration2
    # make sure that a<b
    if a > b:
        print('Incorrect bounds')
        return None
    # ok now we can start
    else:
        # Make n to be even if not
        if n%2 != 0: 
            n = n+1
        # compute your midpoint
        h = (b - a)/float(n)
        # initialize your sum
        sum1 = 0
        iteration2 += 1
        # iterate through necesarry number of times
        # in order to get as accurate as possible
        for i in range(1, int(n/2 + 1)):
            # add value to sum1
            sum1 += f(a + (2*i - 1)*h)
            iteration2 += 1
        # cheat alittle
        sum1 *= 4
        # lets try this again
        sum2 = 0
        iteration2 +=1
        # loop through and do it again for different eval
        for i in range(1, int(n/2)):
            sum2 += f(a + 2*i*h)
            iteration2 += 1
        # cheat alittle
        sum2 *= 2
        # get our best approximation
        approx = (b - a)/(3.0*n)*(f(a) + f(b) + sum1 + sum2)
        print ('Simpson result: ' + str(round(approx,8)))
        # get actual to find out error
        actual = integrate.quad(f, 0, 1)[0]
        # compute error
        error = round(abs(actual - approx), 8)
        print ('Simpson error: ' + str(error))
        print('Trapezoidal Iteration Count: ' + str(iteration2))


def newtTrapSimp(func, a, b, n):
    global iteration, iteration2
    #### SIMPSON
    newtonSimpson(func, a, b, n)

    ### TRAPEZOIDAL
    newtonTrapezoidal(func, a, b, n)
    print("The total iteration count is: " + str(iteration+iteration2))


if __name__ == '__main__':
    func = lambda x: x**2
    a = 0.0
    b = 1.0
    n = 4

    newtTrapSimp(func, a, b, n)

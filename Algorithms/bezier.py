import numpy as np
from math import *
from sympy import *
from scipy import interpolate
from scipy.misc import comb
from matplotlib import pyplot as plt


def bernstein_poly(i, n, t):
    """
     The Bernstein polynomial of n, i as a function of t
    """

    return comb(n, i) * ( t**(n-i) ) * (1 - t)**i


def bezier_curve(points, nTimes=1000):
    """
       Given a set of control points, return the
       bezier curve defined by the control points.

       points should be a list of lists, or list of tuples
       such as [ [1,1],
                 [2,3],
                 [4,5], ..[Xn, Yn] ]
        However, we aware that the function takes in input as they come. So, if the points
        are not ordered correctly, you will get incorrect results. 
        Should be: [ [x1,y1],
                     [x2,y2],
                     ........[xn,yn] ]
        nTimes is the number of time steps, defaults to 1000

    """

    nPoints = len(points)
    xPoints = np.array([p[0] for p in points])
    yPoints = np.array([p[1] for p in points])



    t = np.linspace(0.0, 1.0, nTimes)

    polynomial_array = np.array([ bernstein_poly(i, nPoints-1, t) for i in range(0, nPoints)   ])

    xvals = np.dot(xPoints, polynomial_array)
    yvals = np.dot(yPoints, polynomial_array)

    return xvals, yvals, xPoints, yPoints

def bezier_spline(xPoints, yPoints, numPoints):
    t = symbols('t')
    if numPoints <= 3:
        print("Enter atleast two control point and one pass through point!\n")
    elif numPoints == 4:
        bx = 3 * (xPoints[1] - xPoints[0])
        cx = 3 * (xPoints[2] - xPoints[1]) - bx
        dx = xPoints[3]-xPoints[0]-bx-cx
        by = 3 * (yPoints[1] - yPoints[0])
        cy = 3 * (yPoints[2] - yPoints[1]) - by
        dy = (yPoints[3]-yPoints[0])-by-cy
        print('x(t) = ' + latex(xPoints[0] + bx * t + cx * t ** 2 + dx * t ** 3))
        print('y(t) = ' + latex(xPoints[0]+by*t+cy*t**2+dy*t**3))
    else:
        print("This is an invalid entry. Sorry, please try again.\n")


# understand  you must enter 4 points.
# if you do not enter 4 points the function will
# reject. If you have equations to enter, please enter the points
# in the form
def bezier(user_input, n=4):
    point = '(';
    foundPoint = False;
    userString = str(user_input);
    try:
        if userString.find(point) != -1:
            foundPoint = True;
        if(foundPoint):
            points = np.array(user_input)
            xvals, yvals, xPoints, yPoints = bezier_curve(user_input, nTimes=1000)
            bezier_spline(xPoints, yPoints, n)
            plt.plot(xvals, yvals)
            plt.plot(xPoints, yPoints, "ro")
            for nr in range( len(user_input)):
                plt.text(xPoints[nr], yPoints[nr], nr)

            plt.show()
        else:
            length = len(user_input)
            xPoints = np.array(user_input[0])
            yPoints = np.array(user_input[1])
            if length == 3:
                zPoints = np.array(user_input[2])
                x1,y1,z1 = xPoints[0],yPoints[0],zPoints[0]
                bx = xPoints[1]
                x2 = eval('(bx+3*x1)/3')
                cx = xPoints[2]
                x3 = eval('(cx+3*x2+bx)/3')
                dx = xPoints[3]
                x4 = eval('dx+x1+bx+cx')
                by = yPoints[1]
                y2 = eval('(by+3*y1)/3')
                cy = yPoints[2]
                y3 = eval('(cy+3*y2+by)/3')
                dy = yPoints[3]
                y4 = eval('dy+y1+by+cy')
                bz = zPoints[1]
                z2 = eval('(bz+3*z1)/3')
                cz = zPoints[2]
                z3 = eval('(cz+3*z2+bz)/3')
                dz = zPoints[3]
                z4 = eval('dz+z1+bz+cz')
                print('Knots: (' + str(x1) + ',' + str(y1) + ',' + str(z1) + ')'+','\
                '(' + str(x4) + ',' + str(y4) + ',' + str(z4) + ')')
                print('Control Points: (' + str(x2) + ',' + str(y2) + ',' + str(z2) + ')'+','\
                '(' + str(x4) + ',' + str(y3) + ',' + str(z3) + ')')
            elif length == 2:
                x1, y1 = xPoints[0], yPoints[0]
                bx = xPoints[1]
                x2 = eval('(bx+3*x1)/3')
                cx = xPoints[2]
                x3 = eval('(cx+3*x2+bx)/3')
                dx = xPoints[3]
                x4 = eval('dx+x1+bx+cx')
                by = yPoints[1]
                y2 = eval('(by+3*y1)/3')
                cy = yPoints[2]
                y3 = eval('(cy+3*y2+by)/3')
                dy = yPoints[3]
                y4 = eval('dy+y1+by+cy')
                print('Knots: (' + str(x1) + ',' + str(y1) + ')' + ',' + '(' + str(x4) + ',' +
                str(y4) + ')')
                print('Control Points: (' + str(x2) + ',' + str(y2) +')' + ','+ '(' + str(x4) + ',' + str(
                    y3) + ')')
            else:
                print("Sorry, you can only use a maximum of 3 equations\n")

    except:
        e = sys.exc_info()[0]
        write_to_page("<p>Error: %s</p>" % e)
        print('Sorry, you have not entered correct input\n')
        return -1


# def main():
#     # nPoints = 4
#     # points = np.random.rand(nPoints,2)*200
#     nPoints = 4
#     points =
#     bezier([[1,0,6,2],[1,-1,0,1],[1,1,6,0]], 4)
#
#
#
# if __name__ == '__main__':
#     main()

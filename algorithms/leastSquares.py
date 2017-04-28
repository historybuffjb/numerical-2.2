import numpy
import sys
import time
import matplotlib.pyplot as plt

# This function takes values in the form of leastSquares(x=[(x,y), (x,y), (x,y)....], y=0, n=numDegree)
# or in the form leastSquares(x=[[1 1], [1 1], [1 1]], y=[1, 1, 1], n=length of array)
# If incorrect output entered this will exit and give you the reason why
# it should, upon correct input, output the least squares equation, coefficients, and the 2 norm error
# for the inputted data, and will also plot a graph if necessary
def leastSquares(x, y, n):
    start = time.time()
    # we need to check what type of input we are dealing with
    # check and return true if one of the two types of correct
    # data entry methods are used
    point = '('
    bracket = '['
    foundPoint = False
    foundBracket = False
    strX = str(x)
    strY = str(y)
    try:
        # if a ( found, evaluate as a series of points
        if strX.find(point) != -1:
            foundPoint = True
        # if a [ found, evaluate as a Ax=b equation using QR factorization
        elif strX.find(bracket) != -1:
            foundBracket = True
        # if this is a series of points
        if foundPoint == True:
            # get all the points
            points = numpy.array(x)
            # get the x and y values respectively
            x_coordinate = points[:,0]
            y_coordinate = points[:,1]
            # get a linear fit for the data
            polyFit = numpy.polyfit(x_coordinate, y_coordinate,n)
            # initialize some variables to calculate the error
            temp = 0.0
            error = 0.0
            # error evaluated using y-line(mx+b)=error for each i
            for i in range(len(x_coordinate)):
                temp=x_coordinate[i]*polyFit[0] + polyFit[1]
                # square each value and add to error
                error += (float(y_coordinate[i]) - float(temp))**2
            # convert polyfit to a formatted line
            f = numpy.poly1d(polyFit)
            root_mean_squared = numpy.sqrt(error) / numpy.sqrt(n)
            print("The least squares fit equation is: " + str(f))
            print("The 2norm error is: " + str(error))
            print("RMSE: " + str(root_mean_squared))
            end = time.time() - start
            print("This function took " + str(end) + " seconds to complete.")
            # plot the best fit line along with all of the points
            # polyFit[0]*x_coordinate+polyFit[1]
            counter = len(polyFit) - 1
            y_fit = 0
            for i in range(0,len(polyFit)):
                y_fit += polyFit[i]*x_coordinate**counter
                counter -= 1
            plt.plot(x_coordinate, y_fit, '-')
            plt.plot(x_coordinate, y_coordinate, 'ro')
            plt.xlabel('X Value')
            plt.ylabel('Y Value')
            # i like grid graphs
            return x_coordinate, y_coordinate, y_fit
        # if data in the form Ax=b
        elif foundBracket == True:
            # calculate using qr factorization
            result = numpy.linalg.lstsq(x,y)
            # it should output coefficient, residual, and rank.
            # we only care about the coefficients and residuals
            # first get the coefficient array
            bracketString = str(result).split('),')
            # create a string that only includes the coefficients
            newstr = bracketString[0].replace('(array(', "")
            root_mean_squared = numpy.sqrt(result[1])/numpy.sqrt(n)
            print("Best fit coefficients: " + newstr)
            print("2-norm Error: " + str(result[1]))
            print("RMSE: " + str(root_mean_squared))
            end = time.time() - start
            print("This function took " + str(end) + " seconds to complete.")
            # find out how much time this all took
            return -1
        # if by some miracle no exception thrown but output still incorrect
        else:

            print('Sorry, you have not entered correct input')
            return -1
    # if incorrect input throw error, tell why
    except:
        e = sys.exc_info()[0]
        write_to_page("<p>Error: %s</p>" % e)
        print('Sorry, you have not entered correct input')
        return -1

# def main():
#     start = time.time()
#     leastSquares([(1.49, 44.6), (3.03, 57.8), (0.57, 49.9), (5.74, 61.3), (3.51, 49.6),(3.73, 61.8), (2.98, 49.0), (-0.18, 44.7), (6.23, 59.2), (3.38, 53.9), (2.15, 46.5),(2.10, 54.7), (3.93, 50.3), (2.47, 51.2), (-0.41, 45.7)],0,2)
#     #leastSquares([(-1,1), (0,0), (1,0), (2,-2)], 0,2)
#     #leastSquares([[1, 1], [1, -1], [1, 1]], [2, 1, 3], 3)
#     end = time.time() - start
#     print("This function took " + str(end) + " seconds to complete.")
#
# if __name__ == '__main__':
#     main()


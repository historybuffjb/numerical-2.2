from scipy.integrate.quadrature import quadrature
from scipy.integrate import quad

def gaussian(f, a, b, y=None):
    try:
        if y:
            y_est, err_est = quadrature(f, a, b, args=(y))
            y_actual, err_actual = quad(f, a, b, args=(y))
            err = err_est + err_actual
        else:
            y_est, err_est = quadrature(f, a, b)
            y_actual, err_actual = quad(f, a, b)
            err = err_est + err_actual

        y_est = round(y_est, 8)
        y_actual = round(y_actual, 8)
        err = round(err, 8)

        print('Estimated value: ' + str(y_est))
        print('Actual value: ' + str(y_actual))
        print('Error: ' + str(err))
    except Exception as e:
        print(str(e))
        print('There was an error. Please verify your input.')

# gaussian(tan, -10, 10)
# gaussian(lambda x: (x**2 * log(x)), 1, 3)

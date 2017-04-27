import math


# Runs the Chebyshev algorithm up to 30 times, increasing degree n until the guess is sufficiently close.
# Outputs the calculated Chebyshev value, the degree of the polynomial where the best guess was calculated,
# and the actual value from the function.
# Example usage: chebyshev(-1, 1, 0.5, math.sin)
# Example output:
# Best Chebyshev value: 0.4796783062232612
# Degree of accurate guess: 4
# Actual function value: 0.479425538604203
def chebyshev(a, b, x, func):
    actual_value = func(x)

    for n in range(1, 30):
        # Calculate roots using 1/2 * b - a and 1/2 b + a
        bma = 0.5 * (b - a)
        bpa = 0.5 * (b + a)

        try:
            f = [func(math.cos(math.pi * (k + 0.5) / n) * bma + bpa) for k in range(n)]
        except ValueError:
            print('Invalid interval. Make sure the function can support negative values.')
            return

        fac = 2.0 / n
        c = [fac * sum([f[k] * math.cos(math.pi * j * (k + 0.5) / n)
             for k in range(n)]) for j in range(n)]

        if not a <= x <= b:
            print('Invalid input. a <= x <= b')
            return

        y = (2.0 * x - a - b) * (1.0 / (b - a))
        y2 = 2.0 * y
        (d, dd) = (c[-1], 0)             # Special case first step for efficiency
        for cj in c[-2:0:-1]:            # Clenshaw's recurrence
            (d, dd) = (y2 * d - dd + cj, d)

        # Calculate the guess
        guess = y * d - dd + 0.5 * c[0]

        # Check if it's close
        if math.isclose(actual_value, guess, rel_tol=0.001):
            print('Best Chebyshev value: ' + str(guess))
            print('Degree of accurate guess: ' + str(n))
            print('Actual function value: ' + str(func(x)))
            return
        elif n == 30:
            print('Error: Could not solve within 30 degrees.')

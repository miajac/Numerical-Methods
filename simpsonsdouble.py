# -*- coding: utf-8 -*-
"""SimpsonsDouble.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1kgPKY-cqr_x9BBojVjqZTYnq84othKE7
"""

import numpy as np

def simpsons_double_integral(a, b, m, n, f, c, d):
    # Step 1: Define step size for x
    h = (b - a) / n
    J1, J2, J3 = 0, 0, 0  # Initialize accumulators for end, even, and odd terms
    # Step 2: Loop over i from 0 to n (for x values)
    for i in range(n + 1):
        x = a + i * h  # Step 3: Current x value
        HX = (d(x) - c(x)) / m  # Step size for y
        # Initialize terms for Simpson's rule over y at fixed x
        K1 = f(x, c(x)) + f(x, d(x))  # End terms
        K2, K3 = 0, 0  # Even and odd terms
        # Step 4: Loop over j from 1 to m-1 (for y values)
        for j in range(1, m):
            y = c(x) + j * HX  # Step 5: Current y value
            Q = f(x, y)  # Evaluate f(x, y)
            # Step 6: Accumulate K2 or K3 based on whether j is even or odd
            if j % 2 == 0:
                K2 += Q
            else:
                K3 += Q
        # Step 7: Compute L for this x slice using Simpson's rule over y
        L = (K1 + 2 * K2 + 4 * K3) * HX / 3
        # Step 8: Accumulate J1, J2, J3 based on the position of i
        if i == 0 or i == n:
            J1 += L
        elif i % 2 == 0:
            J2 += L
        else:
            J3 += L
    # Step 9: Calculate the final approximation J
    J = h * (J1 + 2 * J2 + 4 * J3) / 3
    # Step 10: Output the result
    return J

import numpy as np
def f(x, y):
    return np.sqrt(x*y + y**2)
# Define the lower and upper bounds for y as functions of x
def c(x):
    return (3*x)-2 # Lower bound for y
def d(x):
    return 6-x  # Upper bound for y
# Integration limits for x and the number of subintervals
a = 2
b = 4
m = 2 # Number of subintervals for y
n = 2  # Number of subintervals for x

result = simpsons_double_integral(a, b, m, n, f, c, d)
print("Approximate integral:", result)

import numpy as np

def simpsons_double_integral(a, b, m, n, f, c, d):
    h = (b - a) / n
    J1, J2, J3 = 0, 0, 0

    for i in range(n + 1):
        x = a + i * h
        HX = (d(x) - c(x)) / m
        K1 = f(x, c(x)) + f(x, d(x))
        K2, K3 = 0, 0

        for j in range(1, m):
            y = c(x) + j * HX
            Q = f(x, y)
            if j % 2 == 0:
                K2 += Q
            else:
                K3 += Q

        L = (K1 + 2 * K2 + 4 * K3) * HX / 3
        if i == 0 or i == n:
            J1 += L
        elif i % 2 == 0:
            J2 += L
        else:
            J3 += L

    J = h * (J1 + 2 * J2 + 4 * J3) / 3
    return J
def f(x, y):
    return np.cos(x)
def c(x):
    return 0  # Lower bound for y

def d(x):
    return x  # Upper bound for y
a = 0
b = np.pi
exact_value = -2
tolerance = 1e-6

n = m = 2  # Initial value, Simpson's method requires even integers

# Increment n and m until the approximation is within the tolerance
while True:
    result = simpsons_double_integral(a, b, m, n, f, c, d)
    error = abs(result - exact_value)

    if error < tolerance:
        break
    n += 2
    m += 2

print(f"Smallest n = m for desired accuracy: {n}")
print(f"Approximate integral: {result}")
print(f"Error: {error}")

#Gaussian Triple
import numpy as np
def f(x, y, z):
    return y**2 *z
def gaussian_triple_integral(a, b, m, n, p, roots, coefficients, alpha, beta, c, d):
    h1 = (b - a) / 2
    h2 = (b + a) / 2
    J = 0
    for i in range(1, m + 1):
        JX = 0
        x = h1 * roots[i - 1] + h2
        d1 = d(x)
        c1 = c(x)
        k1 = (d1 - c1) / 2
        k2 = (d1 + c1) / 2
        for j in range(1, n + 1):
            JY = 0
            y = k1 * roots[j - 1] + k2
            beta1 = beta(x, y)
            alpha1 = alpha(x, y)
            l1 = (beta1 - alpha1) / 2
            l2 = (beta1 + alpha1) / 2
            for k in range(1, p + 1):
                z = l1 * roots[k - 1] + l2
                Q = f(x, y, z)
                JY += coefficients[k - 1] * Q
            JX += coefficients[j - 1] * l1 * JY
        J += coefficients[i - 1] * k1 * JX
    J *= h1
    return J

a = 0  # Lower limit for x
b = 1  # Upper limit for x
m = 3  # Number of intervals for x
n = 3  # Number of intervals for y
p = 3  # Number of intervals for z

roots = np.array([-np.sqrt(3/5), 0, np.sqrt(3/5)])  # Roots for 3-point quadrature
coefficients = np.array([5/9, 8/9, 5/9])  # Weights for 3-point quadrature

def alpha(x, y):
    return 0
def beta(x, y):
    return y
def c(x):
    return x
def d(x):
    return 1

result = gaussian_triple_integral(a, b, m, n, p, roots, coefficients, alpha, beta, c, d)
print("Approximate integral:", result)
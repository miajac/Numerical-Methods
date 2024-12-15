# -*- coding: utf-8 -*-
"""CubicSpline.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1W61zQRTTHm2a9MwaXjSQQM2aH7wUU_nC
"""

##Natural
import numpy as np

def natural_cubic_spline(x, a):
    n = len(x) - 1  # n is the number of intervals
    h = np.diff(x)   # h_i = x_{i+1} - x_i

    # Step 2: Compute α
    alpha = np.zeros(n)
    for i in range(1, n):
        alpha[i] = (3/h[i]) * (a[i+1] - a[i]) - (3/h[i-1]) * (a[i] - a[i-1])

    # Step 3-6: Solve the tridiagonal system
    l = np.ones(n+1)
    mu = np.zeros(n+1)
    z = np.zeros(n+1)
    c = np.zeros(n+1)

    # Forward sweep
    for i in range(1, n):
        l[i] = 2 * (x[i+1] - x[i-1]) - h[i-1] * mu[i-1]
        mu[i] = h[i] / l[i]
        z[i] = (alpha[i] - h[i-1] * z[i-1]) / l[i]

    # Boundary conditions
    l[n] = 1
    z[n] = 0
    c[n] = 0

    # Back substitution
    b = np.zeros(n)
    d = np.zeros(n)

    for j in range(n-1, -1, -1):
        c[j] = z[j] - mu[j] * c[j+1]
        b[j] = (a[j+1] - a[j]) / h[j] - h[j] * (c[j+1] + 2 * c[j]) / 3
        d[j] = (c[j+1] - c[j]) / (3 * h[j])

    return a[:-1], b, c[:-1], d

x = np.array([0.1,0.2,0.3,0.4])  # input x data
a = np.array([-0.62049958,-0.28398668,0.00660095,0.2484244])  # input f(x) data

aj, bj, cj, dj = natural_cubic_spline(x, a)

print("aj:", aj)
print("bj:", bj)
print("cj:", cj)
print("dj:", dj)

#Cubic spline
import numpy as np

def clamped_cubic_spline(x, y, FPO, FPN):
    n = len(x) - 1
    h = np.diff(x)
    # Step 2: Compute the alpha values
    alpha = [0] * (n + 1)
    alpha[0] = ((3 * (y[1] - y[0])) / h[0]) - 3 * FPO
    alpha[n] = 3 * FPN - (3 * (y[n] - y[n-1]) / h[n-1])

    for i in range(1, n):
        alpha[i] = (3 / h[i]) * (y[i+1] - y[i]) - (3 / h[i-1]) * (y[i] - y[i-1])

    # Step 3: Set up l, mu, and z arrays
    l = [0] * (n + 1)
    mu = [0] * (n + 1)
    z = [0] * (n + 1)

    l[0] = 2 * h[0]
    mu[0] = 0.5
    z[0] = alpha[0] / l[0]

    for i in range(1, n):
        l[i] = 2 * (x[i+1] - x[i-1]) - h[i-1] * mu[i-1]
        mu[i] = h[i] / l[i]
        z[i] = (alpha[i] - h[i-1] * z[i-1]) / l[i]

    l[n] = h[n-1] * (2 - mu[n-1])
    z[n] = (alpha[n] - h[n-1] * z[n-1]) / l[n]


    # Step 4: Initialize coefficient arrays
    a = [y[i] for i in range(n+1)]
    b = [0] * n
    c = [0] * (n+1)
    d = [0] * n

    c[n] = z[n]

    # Step 5: Compute coefficients b, c, d
    for j in range(n-1, -1, -1):
        c[j] = z[j] - mu[j] * c[j+1]
        b[j] = (y[j+1] - y[j]) / h[j] - h[j] * (c[j+1] + 2 * c[j]) / 3
        d[j] = (c[j+1] - c[j]) / (3 * h[j])

    # Step 6: Return the coefficients
    return a[:-1], b, c[:-1], d

x_vals = [-0.25,0.25]
y_vals = [1.33203,0.800781]
FPO = 0.4375 # Derivative at x0
FPN = -0.625 # Derivative at xn

a, b, c, d = clamped_cubic_spline(x_vals, y_vals, FPO, FPN)

print("a coefficients:", a)
print("b coefficients:", b)
print("c coefficients:", c)
print("d coefficients:", d)
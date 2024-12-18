# -*- coding: utf-8 -*-
"""AdaptiveQuadrature.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1KmLr_zw9EVChF4jwwY2i8IdmEtYMMfa7
"""

import math

# Define the function f(x)
def f(x):
    return (((6*math.cos(4*x))+(4*math.sin(6*x)))*math.exp(x))

# Adaptive quadrature function
def adaptive_quadrature(f, a, b, tol, N):
    # Initial setup
    app = 0.0
    i = 1
    tol_i = 10 * tol
    ai = a
    hi = (b - a) / 2
    FAi = f(a)
    FCi = f(a + hi)
    FBi = f(b)
    Si = hi * (FAi + 4 * FCi + FBi) / 3  # Initial Simpson's rule estimation
    Li = 1

    # Stack to hold subinterval data at each level
    stack = [(ai, FAi, FCi, FBi, hi, tol_i, Si, Li)]

    while i > 0:
        # Step 3: Evaluate function at points for Simpson’s method on halves
        ai, FAi, FCi, FBi, hi, tol_i, Si, Li = stack.pop()
        FD = f(ai + hi / 2)
        FE = f(ai + 3 * hi / 2)
        S1 = hi * (FAi + 4 * FD + FCi) / 6
        S2 = hi * (FCi + 4 * FE + FBi) / 6

        # Calculate the error estimate
        if abs(S1 + S2 - Si) < tol_i:
            # If within tolerance, add to approximation
            app += S1 + S2
            i -= 1  # Move back a level
        elif Li >= N:
            # If maximum levels are exceeded
            return "LEVEL EXCEEDED"
        else:
            # Step 5: Add data for next level
            i += 1  # Move forward to next level
            # Right-half subinterval data
            stack.append((ai + hi, FCi, FE, FBi, hi / 2, tol_i / 2, S2, Li + 1))
            # Left-half subinterval data
            stack.append((ai, FAi, FD, FCi, hi / 2, tol_i / 2, S1, Li + 1))

    # Step 6: Return the computed approximation
    return app

result = adaptive_quadrature(f, 0,((math.pi)/2), 1e-5, 200)
print("Approximate integral:", result)
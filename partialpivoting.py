# -*- coding: utf-8 -*-
"""partialPivoting.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1DIwjCebZKrtz6N_VxgXHlSOEF2sO8mJz
"""

import numpy as np

def gaussian_elimination_partial_pivoting(A):
    n = len(A)  # Number of unknowns
    NROW = list(range(n))  # Initialize row pointer

    # Step 2: Elimination process
    for i in range(n - 1):
        # Step 3: Find the pivot row
        p = max(range(i, n), key=lambda j: abs(A[NROW[j]][i]))
        if A[NROW[p]][i] == 0:
            print("No unique solution exists.")
            return None

        # Step 4: Swap rows in NROW if necessary
        if NROW[i] != NROW[p]:
            NROW[i], NROW[p] = NROW[p], NROW[i]

        # Step 5: Forward elimination
        for j in range(i + 1, n):
            m = A[NROW[j]][i] / A[NROW[i]][i]
            A[NROW[j]][i:] = A[NROW[j]][i:] - m * A[NROW[i]][i:]

    # Step 6: Check for unique solution in the last row
    if A[NROW[n - 1]][n - 1] == 0:
        print("No unique solution exists.")
        return None

    # Step 7: Back substitution
    x = np.zeros(n)
    x[n - 1] = A[NROW[n - 1]][n] / A[NROW[n - 1]][n - 1]
    for i in range(n - 2, -1, -1):
        x[i] = (A[NROW[i]][n] - sum(A[NROW[i]][j] * x[j] for j in range(i + 1, n))) / A[NROW[i]][i]

    return x

# Example usage
# Define an augmented matrix for a system with n variables
A = np.array([
    [3.14, -2.72, 1.41, -1.73, 3.32],
    [9.87, 2.72, -7.39, 0.429, 0],
    [2.24, -2.45, 1, -1.4, 3.14],
    [31, 7.39, -2.65, 0.111, 1.41]
])

solution = gaussian_elimination_partial_pivoting(A)
if solution is not None:
    print("Solution:", solution)

import numpy as np

def round3(value):
    """Round a value to 3 significant digits."""
    return round(value, 3)

def gaussian_elimination_partial_pivoting_3digit(A):
    n = len(A)  # Number of unknowns
    NROW = list(range(n))  # Initialize row pointer

    # Step 2: Elimination process
    for i in range(n - 1):
        # Step 3: Find the pivot row
        p = max(range(i, n), key=lambda j: abs(A[NROW[j]][i]))
        if round3(A[NROW[p]][i]) == 0:
            print("No unique solution exists.")
            return None

        # Step 4: Swap rows in NROW if necessary
        if NROW[i] != NROW[p]:
            NROW[i], NROW[p] = NROW[p], NROW[i]

        # Step 5: Forward elimination
        for j in range(i + 1, n):
            m = round3(A[NROW[j]][i] / A[NROW[i]][i])
            for k in range(i, n + 1):
                A[NROW[j]][k] = round3(A[NROW[j]][k] - m * A[NROW[i]][k])

    # Step 6: Check for unique solution in the last row
    if round3(A[NROW[n - 1]][n - 1]) == 0:
        print("No unique solution exists.")
        return None

    # Step 7: Back substitution
    x = np.zeros(n)
    x[n - 1] = round3(A[NROW[n - 1]][n] / A[NROW[n - 1]][n - 1])
    for i in range(n - 2, -1, -1):
        sum_ax = sum(round3(A[NROW[i]][j] * x[j]) for j in range(i + 1, n))
        x[i] = round3((A[NROW[i]][n] - sum_ax) / A[NROW[i]][i])

    return x

# Example usage
# Define an augmented matrix for a system with n variables
A = np.array([
    [(np.pi()), (-1*np.exp()), (np.sqrt(2)), (-1*np.sqrt(3)), (np.sqrt(11))],
    [np.pi**2, np.exp(), -1*np.exp**2, (3/7)],
    [np.sqrt(5), -1*np.sqrt(6), 1, -1*np.sqrt(2), np.pi()],
    [np.pi()**3, np.exp()**2, -1*np.sqrt(7), (1/9), np.sqrt(2)]
])

solution = gaussian_elimination_partial_pivoting_3digit(A)
if solution is not None:
    print("Solution:", solution)
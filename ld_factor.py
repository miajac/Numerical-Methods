# -*- coding: utf-8 -*-
"""LD_factor.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14lasNXvgdJmO_u5j8UtDdOLH7Yuzetj5
"""

import numpy as np

def lu_factorization_and_solve(A):
    n = A.shape[0]
    if A.shape[1] != n + 1:
        raise ValueError("Matrix A must be an n x (n+1) augmented matrix.")
    # Separate the matrix A into coefficients and the augmented column b
    b = A[:, -1]
    A = A[:, :-1]
    L = np.eye(n)  # Lower triangular matrix (identity initially)
    U = np.zeros_like(A, dtype=float)  # Upper triangular matrix
    # LU Decomposition
    for i in range(n):
        if A[i, i] == 0:
            raise ValueError(f"Factorization impossible, zero pivot encountered at row {i}.")
        U[i, i:] = A[i, i:] - np.dot(L[i, :i], U[:i, i:])
        for j in range(i + 1, n):
            L[j, i] = (A[j, i] - np.dot(L[j, :i], U[:i, i])) / U[i, i]
    # Solve Ly = b using forward substitution
    y = np.zeros(n, dtype=float)
    for i in range(n):
        y[i] = b[i] - np.dot(L[i, :i], y[:i])
    # Solve Ux = y using backward substitution
    x = np.zeros(n, dtype=float)
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - np.dot(U[i, i + 1:], x[i + 1:])) / U[i, i]
    return L, U, x
# Usage
if __name__ == "__main__":
    A = np.array([
        [2.121,-3.46,0,5.217,1.909],
        [0,5.193,-2.197,4.206,0],
        [5.132,1.414,3.141,0,-2.101],
        [-3.111,-1.732,2.718,5.212,6.824]
    ], dtype=float)

    try:
        L, U, x = lu_factorization_and_solve(A)
        print("Lower triangular matrix L:")
        print(L)
        print("\nUpper triangular matrix U:")
        print(U)
        print("\nSolution x:")
        print(x)
    except ValueError as e:
        print(e)
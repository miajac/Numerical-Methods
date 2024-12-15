# -*- coding: utf-8 -*-
"""Coombs_BisectionMethod.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1eM_H_R2XhO6dDQxteRvG4qJdLWiDTiLd

Programming Assignment 1,
Miaja Coombs,
09/13/2024, shared via google colab
"""

import numpy as np
import matplotlib.pyplot as plt
def polynomial(x):  #Define the polynomial function
    return x*(x*(x+4)*x)-10
def bisection_method(func, a, b, tol, itmax): #Define the bisection method
    if func(a) * func(b) >= 0: #Case where the function does not cross the x-axis in [a, b]
        print(f"Bisection method fails.")
        return None
    p = a #Initialize midpoint variable
    iteration = 0 #Initialize iteration count
    results = [] #Initialize results list
    while (b - a) / 2.0 > tol and iteration < itmax:  #Iterate until max iterations are reached or the value is within tolerance value
        iteration += 1 #Progress through another iteration
        p = (a + b) / 2.0  # Calculate the midpoint of [a,b], midpoint is p
        error = (b - a) / (2 ** iteration)
        results.append([iteration, a, b, p, func(p), error]) #add info to results list iteratively
        if func(p) == 0.0:  # p is the root
            break
        elif func(a) * func(p) < 0: #if f(a)*f(p) is negative, interval becomes [a,p], we know that the root is within this interval
            b = p
        else:
            a = p #if not, the interval becomes [b,p],
    if iteration == itmax: #implies root was not found within a clear tolerance value in the number of iterations deemed reasonable by the itmax value
        print(f"Reached maximum number of iterations ({itmax})")
    p = (a + b) / 2.0 #one more midpoint
    results.append([iteration + 1, a, b, p, func(p), error]) #add this midpoint to list results
    return p, iteration + 1, results #return final p value, iteration value, and results table
def plot_function(func, a, b): #function for plotting function
    x = np.linspace(a - 1, b + 1, 400)  #x values
    y = func(x)  #y values
    plt.plot(x, y)  #plot function
    plt.axhline(0, color='black',linewidth=0.5)  # x-axis
    plt.axvline(0, color='black',linewidth=0.5)  # y-axis
    plt.xlim(a - 1, b + 1)  #x-axis limits
    plt.xlabel('x')  #x-axis label
    plt.ylabel('f(x)')  #y-axis label
    plt.grid(True)
    plt.show() #plot function
def print_results_table(results): #function creating results table
    print(f"{'Iteration':10} {'a':10} {'b':10} {'p':10} {'f(p)':10} {'Error':15}") #table headings
    for res in results:
        iteration, a_val, b_val, p_val, f_p, error = res
        print(f"{iteration:>10} {a_val:>10.6f} {b_val:>10.6f} {p_val:>10.6f} {f_p:>10.6f} {error:>15.6f}") #results
def main(): #function referencing the bisection method and defining variables used
    a = 1 # lower interval value
    b = 2 #upper interval value
    x = -4 #An option to just change the exponent for the tolerance value, can be commented out (in that case you would just edit tol value)
    tol = 10 ** x #Set a tolerance value
    itmax = 20  # Set a maximum number of iterations
    plot_function(polynomial, a, b) #plot function using polynomial and interval [a,b]
    result = bisection_method(polynomial, a, b, tol, itmax)
    if result is not None: #defines outputs given that a root is determined
        root, iterations, results = result
        print_results_table(results) #print table
        print(f"\nApproximated root: {root}")
        final_error = (b - a) / (2 ** iterations) #final error calculation
        print(f"Upper bound of the error: {final_error}")
main()

"""Question 2:
(a)
1. Root: 1.24029541015625
2. Root: 1.57073974609375
3. a. Root: 2.0000686645507812
   b. Root: -2.0000686645507812
   c. Root: -1.0000839233398438
   d. Root: 1.0000839233398438

"""

import numpy as np
import matplotlib.pyplot as plt
def polynomial(x):  #Define the polynomial function
    return x*(x*(x+4)*x)-10
def bisection_method(func, a, b, tol, itmax): #Define the bisection method
    if func(a) * func(b) >= 0: #Case where the function does not cross the x-axis in [a, b]
        print(f"Bisection method fails.")
        return None
    p_prev = 1 #Initialize pn-1
    p = b #Initialize midpoint variable
    iteration = 0 #Initialize iteration count
    results = [] #Initialize results list
    while abs(p-p_prev)/abs(p) <tol and iteration < itmax:  #Iterate until max iterations are reached or the value is within tolerance value
        iteration += 1 #Progress through another iteration
        p = (a + b) / 2.0  # Calculate the midpoint of [a,b], midpoint is p
        error = (b - a) / (2 ** iteration)
        results.append([iteration, a, b, p, func(p), error]) #add info to results list iteratively
        if func(p) == 0.0:  # p is the root
            break
        elif func(a) * func(p) < 0: #if f(a)*f(p) is negative, interval becomes [a,p], we know that the root is within this interval
            b = p
        else:
            a = p #if not, the interval becomes [b,p]
        p_prev = p #update p
    if iteration == itmax: #implies root was not found within a clear tolerance value in the number of iterations deemed reasonable by the itmax value
        print(f"Reached maximum number of iterations ({itmax})")
    p = (a + b) / 2.0 #one more midpoint
    error = (b - a) / 2.0
    results.append([iteration + 1, a, b, p, func(p), error]) #add this midpoint to list results
    return p, iteration + 1, results #return final p value, iteration value, and results table
def plot_function(func, a, b): #function for plotting function
    x = np.linspace(a - 1, b + 1, 400)  #x values
    y = func(x)  #y values
    plt.plot(x, y)  #plot function
    plt.axhline(0, color='black',linewidth=0.5)  # x-axis
    plt.axvline(0, color='black',linewidth=0.5)  # y-axis
    plt.xlim(a - 1, b + 1)  #x-axis limits
    plt.xlabel('x')  #x-axis label
    plt.ylabel('f(x)')  #y-axis label
    plt.grid(True)
    plt.show() #plot function
def print_results_table(results): #function creating results table
    print(f"{'Iteration':10} {'a':10} {'b':10} {'p':10} {'f(p)':10} {'Error':15}") #table headings
    for res in results:
        iteration, a_val, b_val, p_val, f_p, error = res
        print(f"{iteration:>10} {a_val:>10.6f} {b_val:>10.6f} {p_val:>10.6f} {f_p:>10.6f} {error:>15.6f}") #results
def main(): #function referencing the bisection method and defining variables used
    a = 1 # lower interval value
    b = 2 #upper interval value
    x = -4 #An option to just change the exponent for the tolerance value, can be commented out (in that case you would just edit tol value)
    tol = 10 ** x #Set a tolerance value
    itmax = 20  # Set a maximum number of iterations
    plot_function(polynomial, a, b) #plot function using polynomial and interval [a,b]
    result = bisection_method(polynomial, a, b, tol, itmax)
    if result is not None: #defines outputs given that a root is determined
        root, iterations, results = result
        print_results_table(results) #print table
        print(f"\nApproximated root: {root}")
        final_error = (b - a) / (2 ** iterations) #final error calculation
        print(f"Upper bound of the error: {final_error}")
main()

"""Question 2b:
The result was stopped on the first iteration because it was larger than the tolerance value. Even if you started using this stopping criteria after the first iteration, it still would be higher than the tolerance value. This produced an approximated root with a very large upper bound of error.

Question 2c: Through this project I learned how to program the bisection method using Python. This process allowed me to analyze this method more thoroughly and to understand both it's selling points and limitations. I also learned how to program tables in python and how to ensure that the stopping criteria used for a program is best suited for the given function and Method. I found this interesting because, initially, I thought that the second stopping criteria would work just fine. However, after analyzing the p values, I recognized that we would either need to have a higher tolerance value or use a different method that was less dependent on suitable p values.
"""
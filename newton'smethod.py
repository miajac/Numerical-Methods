# -*- coding: utf-8 -*-
"""Newton'sMethod.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1y2jE2BmCbcV6XDhKgTpEVKxPlEY4KD9y
"""

def NewtonsMethod(func, df, p0, tol, itmax):
    i = 1
    while i <= itmax:
        p = p0 - func(p0) / df(p0)
        print(f"Iteration {i}: p = {p}")
        if abs(p - p0) < tol:
            print(f"Converged to p = {p} after {i} iterations")
            return p
        p0 = p
        i += 1
    print("Maximum number of iterations reached")
    return

def NewtonsMethodAlt(func, df, p0, tol, itmax):
    i = 1
    while i <= itmax:
        p = p0 - func(p0) / df(p0)
        print(f"Iteration {i}: p = {p}")
        if abs(p - p0) < tol:
            print(f"Converged to p = {p} after {i} iterations")
            return p
        p0 = p
        i += 1
    print("Maximum number of iterations reached")
    return

import numpy as np
def f(x):
  return np.cos(x-1)
def fd(x):
  return 6*np.exp(6*x) + 6*(np.log(2)**2)*np.exp(2*x) - 4*np.log(8)*np.exp(4*x)

NewtonsMethod(f,fd,0,0.0002,100)

def Steffensens(func,p0,tol,itmax):
  i=1
  while i<=itmax:
    p1=f(p0)
    p2=f(p1)
    p=p0-(p1-p0)**2/(p2-2*p1+p0)
    print (f"Iteration {i}: p = {p}")
    if abs(p-p0)<tol:
      print(f"Converged to p = {p} after {i} iterations")
      return p
    i += 1
    p0=p
  print("Max iterations")
  return

Steffensens(f,2,0.0002,100)

def SecantMethod(func,p0,p1,tol,itmax):
  i=2
  q0=func(p0)
  q1=func(p1)
  while i <= itmax:
    p=p1-(q1*(p1-p0))/(q1-q0)
    print(f"Iteration {i}: p = {p}")
    if abs(p-p1)<tol:
      print(f"Converged to p = {p} after {i} iterations")
      return p
    i += 1
    p0=p1
    q0=q1
    p1=p
    q1=func(p)
  print("Maximum number of iterations reached")
  return

def f(x):
  return 2*x +3*np.cos(x) - np.exp(x)

SecantMethod(f,1,2,0.00001,100)

def FalsePosition(func,p0,p1,tol,itmax):
  i=2
  q0=func(p0)
  q1=func(p1)
  while i <= itmax:
    p= p1 - (q1*(p1-p0))/(q1-q0)
    print(f"Iteration {i}: p = {p}")
    if abs(p-p1)<tol:
      print(f"Converged to p = {p} after {i} iterations")
      return p
    i = i+1
    q=func(p)
    if q*q1 < 0:
      p0=p1
      q0=q1
    p1=p
    q1=q
  print("Maximum number of iterations reached")
  return

def f(x):
  return 2*x +3*np.cos(x) - np.exp(x)

FalsePosition(f,1,2,0.00001,100)
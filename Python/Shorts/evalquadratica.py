# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 20:06:32 2020

@author: admin
"""


def evalQuadratic(a, b, c, x):
    """
    

    Parameters
    ----------
    a : NUM
        DESCRIPTION.
    b : NUM
        DESCRIPTION.
    c : NUM
        DESCRIPTION.
    x : NUM
        DESCRIPTION.

    Returns
    -------
    Result of Quadratic Equation (a*x + b*x + c)

    """
    return((a*(x*x)) + (b*x) + c)

print(evalQuadratic(6.72, 1.01, -8.81, -3.4))


def func_a():
    print("inside function a")
def func_b(y):
    print("inside function b")
    return y
def func_c(z):
    print("inside func_c")
    return z()
print(func_a())
print(5 + func_b(2))
print(func_c(func_a))


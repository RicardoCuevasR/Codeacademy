# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 23:26:51 2020

@author: ciadmin
"""


def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
    
    
print(fact(4))


def recurPower(base, exp):
    """
    

    Parameters
    ----------
    base : TYPE
        DESCRIPTION.
    exp : TYPE
        DESCRIPTION.

    Returns
    -------
    Result of the exponentiation in an recursive way

    """
    
    if exp == 0:
        return 1
    #Got rid of the second else, just sending the return out of the if
    return(recurPower(base,exp-1)*base)
    
    
print(recurPower(2.13, 0))

def iterPower(base, exp):
    """
    

    Parameters
    ----------
    base : TYPE
        DESCRIPTION.
    exp : TYPE
        DESCRIPTION.

    Returns
    -------
    Result of the exponentiation in an iterative way

    """
    
    count = 1
    result = base
    while count < exp:
        result *= base    
        count += 1
    return result
    
print(iterPower(4,8))
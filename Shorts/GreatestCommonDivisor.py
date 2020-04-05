# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 11:48:19 2020

@author: ciadmin
"""


def gdcIter(a,b):
    """
    Parameters
    ----------
    a : TYPE
        DESCRIPTION.
    b : TYPE
        DESCRIPTION.

    Returns
    -------
    Shows GDC for two digits in an iterative way.

    """
    gdc = min(a,b)
    while gdc > 0:
        if  a%gdc == 0 and b%gdc == 0:
            return gdc
        else:
            gdc -= 1
        
print(gdcIter(27,81))

def gdcRecur(a,b):
    '''
    Parameters
    ----------
    a : int
        First number.
    b : int
        Second Number.

    Returns
    -------
    Returns GDC fro two digits in a recursive way.

    
    gdc = min(a,b)
    if max(a,b)%gdc == 0 and min(a,b)%gdc == 0:
        return min(a,b)
    return(gdcRecur(max(a,b),(min(a,b)-1)))

print(gdcRecur(12,3))    
'''
    # Base case is when b = 0
    if b == 0:
        return a

    # Recursive case
    return gdcRecur(b, a % b)

print (gdcRecur(3,12))
    
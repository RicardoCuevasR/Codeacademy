# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 14:47:40 2020

@author: ricar

Depending of reverse will send different Results
"""

def printName(firstName, lastName, reverse = False):
    
    """If I define reverse I dont need to pass a value
    
    Remember I can call whatever is in the docstring with:
        help(Name of Function)
    
    """
    if reverse:
        print(lastName, " , ", firstName)
    else:
        print(firstName, " , ", lastName)
        
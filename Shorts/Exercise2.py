# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 15:00:02 2020

@author: ricar
"""

def foo(x, y = 5):
   def bar(x):
      return x + 1
   return bar(y * 2)
          
foo(3, 0)
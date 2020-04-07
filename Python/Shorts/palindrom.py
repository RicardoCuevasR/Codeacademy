# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 22:03:39 2020

@author: ciadmin
"""


def isPalindrome(s):
    '''
    
    Parameters
    ----------
    s : string
        Checks if a string is palidrome or not.

    Returns
    -------
    None.

    '''
    def toChar(s):
        '''
        Parameters
        ----------
        s : sting
        Will get rid of spaces and lower case everything

        
        '''
        s = s.lower()
        ans = ''
        for c  in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans
    
    def isPal(s):
        if len(s) <=1:
            return True
        else:
            return s[0]== s[-1] and isPal(s[1:-1])
        
    return isPal(toChar(s))

print("")
print(isPalindrome('ominoni'))
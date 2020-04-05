def is_even(i):
    """
    Input; i, a positive int
    Returns True if i is even otherwise False
    """
    print("Hi")
    i%2 == 0

print(is_even(3))

''''WARNING' when no return in a funstion is set, the functionn will return None'''

def f(x):
    """
    

    Parameters
    ----------
    x : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    x = x+1
    print('in f(x): x =', x)
    return x
x = 3
z = f(x)

print(z)

# -*- coding: utf-8 -*-

################################################################################################
# 对函数fact(n)编写doctest并执行：
################################################################################################

def fact(n):
    '''
    Function to calculate factorial
    >>> fact(1)
    1
    >>> fact(3)
    6
    >>> fact(10)
    3628800
    >>> fact(-1)
    Traceback (most recent call last):
    ...
    ValueError: n must be equal or greater than 1
    >>> fact('')
    Traceback (most recent call last):
    ...
    ValueError: n must be an integer!
    '''
    if isinstance(n,int):
        if n < 1:
            raise ValueError('n must be equal or greater than 1')
        if n == 1:
            return 1
        return n * fact(n - 1)
    else:
        raise ValueError('n must be an integer!')

if __name__ == '__main__':
    import doctest
    doctest.testmod()
import doctest
from collections import namedtuple

Result = namedtuple('Result', 'count average')

def averager():
    
    """
    A coroutine to compute a running average
    
        >>> coro_avg = averager()
        >>> next(coro_avg)
        >>> coro_avg.send(10)
        >>> coro_avg.send(30)
        >>> coro_avg.send(6.5)
        >>> coro_avg.send(None)
        Traceback (most recent call last):
         ...
        StopIteration: Result(count=3, average=15.5)

    """
    
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total / count
    return Result(count, average)
    
if __name__ == '__main__':
    doctest.testmod(verbose=True)
    

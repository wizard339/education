import doctest

"""
    A coroutine to compute a running average
    
        >>> coro_avg = averager()
        >>> from inspect import getgeneratorstate
        'GEN_SUSPENDED'
        >>> coro_avg.send(10)
        10.0
        >>> coro_avg.send(30)
        20.0
        >> coro_avg.send(5)
        15.0

"""

from couroutil import couroutine

@couroutine
def averager():
    total = 0.0
    count = 0
    averager = None
    while True:
        term = yield averager
        total = += term
        count = +=1
        averager = total/count
        

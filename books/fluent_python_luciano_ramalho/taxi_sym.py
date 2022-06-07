"""
Modelling a taxi
================

Driving a taxi from the console::
    
    >>> from taxi_sim import taxi_process
    >>> taxi = taxi_process(ident=13, trips=2, start_time=0)
    >>> next(taxi)
    Event(time=0, proc=13, action='leave garage')
    >>> taxi.send(_.time + 7)
    Event(time=7, proc=13, action='pick up passenger')
    >>> taxi.send(_.time + 23)
    Event(time=30, proc=13, action='drop off passenger')
    >>> taxi.send(_.time + 5)
    Event(time=35, proc=13, action='pick up passenger')
    >>> taxi.send(_.time + 48)
    Event(time=83, proc=13, action='drop off passenger')
    >>> taxi.send(_.time + 1)
    Event(time=84, proc=13, action='going home')
    >>> taxi.send(_.time + 10)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    StopIteration
    
Simple run with two cars, random seed 10. This is a valid doctest::

    >>> main(num_taxis=2, seed=10)
    taxi: 0 Event(time=0, proc=0, action='leave garage')
    taxi: 0 Event(time=5, proc=0, action='pick up passenger')
    taxi: 1     Event(time=5, proc=1, action='leave garage')
    taxi: 1     Event(time=10, proc=1, action='pick up passenger')
    taxi: 1 Event(time=15, proc=1, action='drop off passenger')
    taxi: 0     Event(time=17, proc=0, action='drop off passenger')
    taxi: 1 Event(time=24, proc=1, action='pick up passenger')
    taxi: 0 Event(time=26, proc=0, action='pick up passenger')
    taxi: 0 Event(time=30, proc=0, action='drop off passenger')
    taxi: 0     Event(time=34, proc=0, action='going home')
    taxi: 1     Event(time=46, proc=1, action='drop off passenger')
    taxi: 1     Event(time=48, proc=1, action='pick up passenger')
    taxi: 1     Event(time=110, proc=1, action='drop off passenger')
    taxi: 1     Event(time=139, proc=1, action='pick up passenger')
    taxi: 1     Event(time=140, proc=1, action='drop off passenger')
    taxi: 1     Event(time=150, proc=1, action='going home')
    *** end of values ***
    
See longer sample run at the end of this module.
    
"""

import random
import collection
import queue
import argparse
import time

DEFAULT_NUMBER_OF_TAXIS = 3
DEFAULT_END_TIME = 180
SEARCH_DARATION = 5
TRIP_DURATION = 20
DEPARTUTE_INTERVAL = 5

Event = collections.namedtuple('Event', 'time proc action')

# BEGIN 
def taxi_process(ident, trips, start_time=0):
    """returns an event to the model every time the state changes """
    pass

# END TAXI_PROCESS

# BEGIN TAXI_SIMULATOR
class Simulator:
    
    def __init__(self, procs_map):
        pass
    
    def run(self, end_time):
        pass
    
# END TAXI_SIMULATOR

def compute_duration(previous_action):
    """computes duration of action using exponential distribution"""
    pass

def main(end_time=DEFAULT_END_TIME, num_taxis=DEFAULT_NUMBER_OF_TAXIS,
         seed=None):
    """initializes a random number generator, builds proc-objects and
       runs a modelling"""
    pass

if __name__=='__main__':
    pass


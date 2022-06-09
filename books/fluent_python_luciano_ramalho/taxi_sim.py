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
    taxi: 0  Event(time=0, proc=0, action='leave garage')
    taxi: 0  Event(time=5, proc=0, action='pick up passenger')
    taxi: 1     Event(time=5, proc=1, action='leave garage')
    taxi: 1     Event(time=10, proc=1, action='pick up passenger')
    taxi: 1     Event(time=15, proc=1, action='drop off passenger')
    taxi: 0  Event(time=17, proc=0, action='drop off passenger')
    taxi: 1     Event(time=24, proc=1, action='pick up passenger')
    taxi: 0  Event(time=26, proc=0, action='pick up passenger')
    taxi: 0  Event(time=30, proc=0, action='drop off passenger')
    taxi: 0  Event(time=34, proc=0, action='going home')
    taxi: 1     Event(time=46, proc=1, action='drop off passenger')
    taxi: 1     Event(time=48, proc=1, action='pick up passenger')
    taxi: 1     Event(time=110, proc=1, action='drop off passenger')
    taxi: 1     Event(time=139, proc=1, action='pick up passenger')
    taxi: 1     Event(time=140, proc=1, action='drop off passenger')
    taxi: 1     Event(time=150, proc=1, action='going home')
    *** end of events ***
    
See longer sample run at the end of this module.
    
"""
import doctest
import random
import collections
import queue
import argparse
import time

DEFAULT_NUMBER_OF_TAXIS = 3
DEFAULT_END_TIME = 180
SEARCH_DURATION = 5
TRIP_DURATION = 20
DEPARTUTE_INTERVAL = 5

Event = collections.namedtuple('Event', 'time proc action')

# BEGIN 
def taxi_process(ident, trips, start_time=0):
    """returns an event to the model every time the state changes """
    time = yield Event(start_time, ident, 'leave garage')
    for i in range(trips):
        time = yield Event(time, ident, 'pick up passenger')
        time = yield Event(time, ident, 'drop off passenger')
        
    yield Event(time, ident, 'going home')
# END TAXI_PROCESS

# BEGIN TAXI_SIMULATOR
class Simulator:
    
    def __init__(self, procs_map):
        self.events = queue.PriorityQueue()
        self.procs = dict(procs_map)
    
    def run(self, end_time):
        """plans and demonstrates events while time will not end"""
        # plan the first event for every car
        for _, proc in sorted(self.procs.items()):
            first_event = next(proc)
            self.events.put(first_event)
            
        # main cycle of modelling
        sim_time = 0
        while sim_time < end_time:
            if self.events.empty():
                print('*** end of events ***')
                break
            
            current_event = self.events.get()
            sim_time, proc_id, previous_action = current_event
            print('taxi:', proc_id, proc_id * '   ', current_event)
            activate_proc = self.procs[proc_id]
            next_time = sim_time + compute_duration(previous_action)
            try:
                next_event = activate_proc.send(next_time)
            except StopIteration:
                del self.procs[proc_id]
            else:
                self.events.put(next_event)
        else:
            msg = '*** end of simulation time:{} events pending ***'
            print(msg.format(self.events.qsize()))
# END TAXI_SIMULATOR

def compute_duration(previous_action):
    """computes duration of action using exponential distribution"""
    if previous_action in ['leave garage', 'drop off passenger']:
        # new state - looking for a passenger
        interval = SEARCH_DURATION
    elif previous_action == 'pick up passenger':
        # new state
        interval = TRIP_DURATION
    elif previous_action == 'going home':
        interval = 1
    else:
        raise ValueError('Unknown previous_action: %s' % previous_action)
    return int(random.expovariate(1/interval)) + 1

def main(end_time=DEFAULT_END_TIME, num_taxis=DEFAULT_NUMBER_OF_TAXIS,
         seed=None):
    """initializes a random number generator, builds proc-objects and
       runs a modelling"""
    if seed is not None:
        random.seed(seed)
        
    taxis = {i: taxi_process(i, (i + 1)*2, i * DEPARTUTE_INTERVAL)
             for i in range(num_taxis)}
    sim = Simulator(taxis)
    sim.run(end_time)

if __name__=='__main__':
    parser = argparse.ArgumentParser(
                        description='Taxi fleet simulator.')
    parser.add_argument('-e', '--end-time', type=int,
                        default=DEFAULT_END_TIME,
                        help='simulation end time, default = %s'
                        % DEFAULT_END_TIME)
    parser.add_argument('-t', '--taxis', type=int,
                        default=DEFAULT_NUMBER_OF_TAXIS,
                        help='number of taxis running, default = %s'
                        % DEFAULT_NUMBER_OF_TAXIS)
    parser.add_argument('-s', '--seed', type=int, default=None,
                        help='random generator seed (for testing)')
    
    args = parser.parse_args()
    main(args.end_time, args.taxis, args.seed)
    doctest.testmod(verbose=True)

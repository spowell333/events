#!/usr/bin/python


import random

from event   import Event
from average import Average

e = Event()
a = Average()


def add_random_sample_delegate(x):
  a.add_sample(x + 10 * (-.5 + random.random()))

def add_sample_delegate(x):
  a.add_sample(x)

e.add_event_listener(add_sample_delegate)
e.add_event_listener(add_random_sample_delegate)

e.add_event(2)
e.add_event(200)


print a.calculate()




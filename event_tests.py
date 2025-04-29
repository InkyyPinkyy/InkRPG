from classes import *
from __main__ import *

def do_random_event(events):
    random_event = random.choice(list(events))
    return random_event


print(do_random_event(events))


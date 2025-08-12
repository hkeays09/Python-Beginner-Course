

# import math # importing the module - gives functions or constant values.
from math import pi
import sys
import random as rdm  # alias for the module
from enum import Enum
import england
from rps7 import rock_paper_scissors
print(pi)

for item in dir(rdm):
    print(item)

print(england.Capital)
england.randomfunfact()

print(__name__)
print(england.__name__)

rock_paper_scissors()

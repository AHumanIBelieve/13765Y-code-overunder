# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Authors:      Chaitya Jain, Kian Conti                                     #
# 	Created:      10/26/2023, 4:41:13 PM                                       #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

# Brain should be defined by default
brain = Brain()
controller = Controller()

brain.screen.print("Hello V5")

while True:
    brain.screen.print("hi")
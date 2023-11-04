# ---------------------------------------------------------------------------- #
# 	Module:       main.py                                                      #
#   Team:         13675Y MTS_CtrlAltDefeat                                     #
# 	Author:       Chaitya Jain                                                 #
# 	Description:  V5 project                                                   #
# ---------------------------------------------------------------------------- #

from vex import *
#import myutils as mu

# Brain should be defined by default
brain = Brain()
controller = Controller()

brain.screen.print("Hello")

#movement funcs

def goForward():
    brain.screen.print("going forward")
    brain.screen.next_row()

def goBack():
    brain.screen.print("going back")
    brain.screen.next_row()

def goLeft():
    brain.screen.print("going left")
    brain.screen.next_row()

def goRight():
    brain.screen.print("going right")
    brain.screen.next_row()

#while loop
while True:
    wait(1, SECONDS)
    if(controller.buttonUp.pressing):
        goForward()
    elif(controller.buttonDown.pressing):
        goBack()
    if(controller.buttonLeft.pressing):
        goLeft()
    elif(controller.buttonRight.pressing):
        goRight()
    brain.screen.print("break")
    brain.screen.next_row()
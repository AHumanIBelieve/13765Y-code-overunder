# ---------------------------------------------------------------------------- #
# 	Module:       main.py                                                      #
#   Team:         13675Y MTS_CtrlAltDefeat                                     #
# 	Author:       Chaitya Jain                                                 #
# 	Description:  V5 project                                                   #
# ---------------------------------------------------------------------------- #

from vex import *
import myutils as mu

# Brain should be defined by default
brain = Brain()
controller = Controller()

brain.screen.print("Hello")

#movement funcs

def goForward():
    mu.sPrint("going forward")

def goBack():
    mu.sPrint("going back")

def goLeft():
    mu.sPrint("going left")

def goRight():
    mu.sPrint("going right")

#while loop
while True:
    if(controller.buttonUp.pressing):
        goForward()
    elif(controller.buttonDown.pressing):
        goBack()
    if(controller.buttonLeft.pressing):
        goLeft()
    elif(controller.buttonRight.pressing):
        goRight()


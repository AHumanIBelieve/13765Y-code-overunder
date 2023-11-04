# ---------------------------------------------------------------------------- #
# 	Module:       main.py                                                      #
#   Team:         13675Y MTS_CtrlAltDefeat                                     #
# 	Author:       Chaitya Jain                                                 #
# 	Description:  V5 project                                                   #
# ---------------------------------------------------------------------------- #

from vex import *
counter = 0
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
    if(controller.buttonUp.pressing == False):
        brain.screen.print("for'rd")
        goForward()
        brain.screen.next_row()
    elif(controller.buttonDown.pressing == True):
        brain.screen.print("back'rd")
        goBack()
        brain.screen.next_row()
    if(controller.buttonLeft.pressing == False):
        goLeft()
        brain.screen.print("lft")
        brain.screen.next_row()
    elif(controller.buttonRight.pressing == False):
        goRight()
        brain.screen.print("rght")
        brain.screen.next_row()
    counter += 1
    if(counter==3):
        brain.screen.clear_screen()
        brain.screen.set_cursor(1, 1)
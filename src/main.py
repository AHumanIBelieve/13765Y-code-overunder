# ---------------------------------------------------------------------------- #
# 	Module:       main.py                                                      #
#   Team:         13675Y MTS_CtrlAltDefeat                                     #
# 	Author:       Chaitya Jain                                                 #
# 	Description:  V5 project                                                   #
# ---------------------------------------------------------------------------- #

from vex import *
counter = 0
#import myutils as mu

# defining stuff
brain = Brain()
controller = Controller()

left_drive = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
right_drive = Motor(Ports.PORT2, GearSetting.RATIO_18_1, True)
drivetrain = DriveTrain(left_drive, right_drive)

brain.screen.print("Hello")
brain.screen.next_row()

# get input funcs

def getXAxisInput():
    inputVal = controller.axis4.position()
    brain.screen.print(inputVal, ", ")

def getYAxisInput():
    inputVal = controller.axis3.position()
    brain.screen.print(inputVal)

def processInputAndReturnMovementAsInts(xAxis, yAxis):
    whereToMove = [0, 0, 0, 0]
    if(xAxis > 0):
        

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
    wait(1000)
    getXAxisInput()
    getYAxisInput()
    brain.screen.next_row()
    counter += 1
    if(counter == 4):
        brain.screen.clear_screen()
        brain.screen.set_cursor(1,1)
        counter = 0
# ---------------------------------------------------------------------------- #
# 	Module:       main.py                                                      #
#   Team:         13675Y MTS_CtrlAltDefeat                                     #
# 	Author:       Chaitya Jain                                                 #
# 	Description:  V5 project                                                   #
# ---------------------------------------------------------------------------- #

from vex import *

# defining stuff
brain = Brain()
controller = Controller()

left_drive_back = Motor(Ports.PORT2, True)
left_drive_front = Motor(Ports.PORT1, True)
left_drive_smart = MotorGroup(left_drive_back, left_drive_front)
right_drive_back = Motor(Ports.PORT9)
right_drive_front = Motor(Ports.PORT10)
right_drive_smart = MotorGroup(right_drive_back, right_drive_front)
drivetrain = DriveTrain(left_drive_smart, right_drive_smart)

brain.screen.print("Hello")
brain.screen.next_row()

# process input from arrow keys
def getXAxisInputButtons():
    inputVal = 0
    if (controller.buttonLeft.pressing()):
        inputVal = -100
    elif (controller.buttonLeft.pressing()):
        inputVal = 100
    return inputVal
def getYAxisInputButtons():
    inputVal = 0
    if (controller.buttonDown.pressing()):
        inputVal = -100
    elif (controller.buttonRight.pressing()):
        inputVal = 100
    return inputVal
def processButtonInputAndReturnMovementAsIntArray(xAxis, yAxis):     
    whereToMove = [0, 0, 0, 0] #move right, left, forward, back
    if(xAxis > 0): #right
        whereToMove[0] = xAxis
    elif(xAxis < 0): #left
        whereToMove[1] = xAxis * -1 #timesed by negative one to make it actually go backwards
    
    if(yAxis > 0): #forward
        whereToMove[2] = yAxis
    elif(yAxis < 0): #back
        whereToMove[3] = yAxis
    
    return whereToMove
def processButtonInputArrayAndCallMovementFuncs(inputArray):
    if(inputArray[2] > 0): #go forward
        goForwardButtons(inputArray[2])
    elif(inputArray[3] < 0): #go backwards
        goBackButtons(inputArray[3])
    else:
        stopMovement()
    
    if(inputArray[0] > 0): # go right
        goRightButtons(inputArray[0])
    elif(inputArray[1] < 0): #go left
        goLeftButtons(inputArray[1])
def goForwardButtons(input):
    drivetrain.drive(FORWARD, input, PERCENT)
    brain.screen.next_row()
def goBackButtons(input):
    drivetrain.drive(REVERSE, input, PERCENT)
    brain.screen.next_row()
def goLeftButtons(input):
    right_drive_smart.spin(FORWARD, input, PERCENT)
    brain.screen.next_row()
def goRightButtons(input):
    left_drive_smart.spin(FORWARD, input, PERCENT)
    brain.screen.next_row()
def stopMovement():
    drivetrain.drive(FORWARD, 0, PERCENT)
    brain.screen.next_row()
def arrowKeyMovement():
    xAxis = getXAxisInputButtons()
    yAxis = getYAxisInputButtons()
    inputArray = processButtonInputAndReturnMovementAsIntArray(xAxis, yAxis)
    brain.screen.print(inputArray)
    processButtonInputArrayAndCallMovementFuncs(inputArray)

#process input from sticks
def getLeftInput():
    inputVal = controller.axis3.value()
    return inputVal

def getRightInput():
    inputVal = controller.axis2.value()
    return inputVal

def Move(vals):
    left_drive_smart.spin(vals[0])
    right_drive_smart.spin(vals[1])

def stickMovement():
    vals = [getLeftInput(), getRightInput()]
    Move(vals)

#while loop
while True:
    wait(10)
    arrowKeyMovement()
    stickMovement()
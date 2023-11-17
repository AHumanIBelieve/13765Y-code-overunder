# ---------------------------------------------------------------------------- #
# 	Module:       main.py                                                      #
#   Team:         13675Y MTS_CtrlAltDefeat                                     #
# 	Author:       Chaitya Jain                                                 #
# 	Description:  V5 project                                                   #
# ---------------------------------------------------------------------------- #

from vex import *
counter = 0

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

# get input funcs

def getXAxisInput():
    inputVal = controller.axis4.position()
    return inputVal

def getYAxisInput():
    inputVal = controller.axis3.position()
    return inputVal

#gets inputs and returns them in an array as numbers between 0 and 100
def processInputAndReturnMovementAsIntArray(xAxis, yAxis):     
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


#movement funcs

def processInputArrayAndCallMovementFuncs(inputArray):
    if(inputArray[2] > 0): #go forward
        goForward(inputArray[2])
    elif(inputArray[3] < 0): #go backwards
        goBack(inputArray[3])
    else:
        stopMovement()
    
    if(inputArray[0] > 0): # go right
        goRight(inputArray[0])
    elif(inputArray[1] < 0): #go left
        goLeft(inputArray[1])

def goForward(input):
    brain.screen.print("going forward")
    drivetrain.drive(FORWARD, input, PERCENT)
    brain.screen.next_row()

def goBack(input):
    brain.screen.print("going back")
    drivetrain.drive(REVERSE, input, PERCENT)
    brain.screen.next_row()

def goLeft(input):
    brain.screen.print("going left")
    right_drive_smart.spin(FORWARD, input, PERCENT)
    brain.screen.next_row()

def goRight(input):
    brain.screen.print("going right")
    left_drive_smart.spin(FORWARD, input, PERCENT)
    brain.screen.next_row()

def stopMovement():
    brain.screen.print("stopping forward/backward")
    drivetrain.drive(FORWARD, 0, PERCENT)
    brain.screen.next_row()

#while loop
while True:
    wait(1000)
    xAxis = getXAxisInput()
    yAxis = getYAxisInput()
    inputArray = processInputAndReturnMovementAsIntArray(xAxis, yAxis)
    brain.screen.print(inputArray)
    processInputArrayAndCallMovementFuncs(inputArray)
    brain.screen.next_row()
    counter += 1
    if(counter == 5):
        brain.screen.clear_screen()
        brain.screen.set_cursor(1,1)
        counter = 0
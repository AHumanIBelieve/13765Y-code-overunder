# ---------------------------------------------------------------------------- #
# 	Module:       main.py                                                      #
#   Team:         13675Y MTS_CtrlAltDefeat                                     #
# 	Author:       Chaitya Jain                                                 #
# 	Description:  V5 project                                                   #
# ---------------------------------------------------------------------------- #

from vex import *
import math

# defining stuff
brain = Brain()
controller = Controller()

right_drive_back = Motor(Ports.PORT9, True)
right_drive_front = Motor(Ports.PORT10, True)
left_drive_back = Motor(Ports.PORT7)
left_drive_front = Motor(Ports.PORT8)
left_drive_smart = MotorGroup(left_drive_back, left_drive_front)
right_drive_smart = MotorGroup(right_drive_back, right_drive_front)
drivetrain = DriveTrain(left_drive_smart, right_drive_smart)
flywheel_motor = Motor(Ports.PORT5)
flywheel_smart = MotorGroup(flywheel_motor)

counter = 0

brain.screen.print("Hello")
brain.screen.next_row()

#process input from sticks
def getLeftInput():
    ogInputVal = controller.axis3.value()
    inputVal = 0
    if(ogInputVal > 0):
        inputVal = (2**(ogInputVal*(math.log(100)/math.log(2))/127))
    elif(ogInputVal < 0):
        ogInputVal = ogInputVal*-1
        inputVal = (2**(ogInputVal*(math.log(100)/math.log(2))/127))
        inputVal = inputVal *-1
    return inputVal

def getRightInput():
    ogInputVal = controller.axis2.value()
    inputVal = 0
    if(ogInputVal > 0):
        inputVal = (2**(ogInputVal*(math.log(100)/math.log(2))/127))
    elif(ogInputVal < 0):
        ogInputVal = ogInputVal*-1
        inputVal = (2**(ogInputVal*(math.log(100)/math.log(2))/127))
        inputVal = inputVal *-1
    return inputVal

def Move(vals):
    left_drive_smart.spin(REVERSE, vals[0], PERCENT)
    right_drive_smart.spin(REVERSE, vals[1], PERCENT)
    brain.screen.print("left: " + str(vals[0]) + "| right: " + str(vals[1]))
    brain.screen.next_row()

def stickMovement():
    vals = [getLeftInput(), getRightInput()]
    Move(vals)

#flywheel code

flywheelSpeed = 0

def flywheel():
    getFlyWheelInput()
    spinFlyWheel()

def getFlyWheelInput():
    global flywheelSpeed
    if(controller.buttonUp.pressing(), flywheelSpeed <100):
        flywheelSpeed = flywheelSpeed + 5
    elif(controller.buttonDown.pressing(), flywheelSpeed > 0):
        flywheelSpeed = flywheelSpeed - 5

def spinFlyWheel():
    flywheel_smart.spin(FORWARD, flywheel, PERCENT)

#while loop
while True:
    wait(10)
    stickMovement()
    flywheel()
    counter = counter +1
    if(counter == 5):
        brain.screen.clear_screen()
        brain.screen.set_cursor(1,1)
        counter = 0
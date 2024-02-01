# ---------------------------------------------------------------------------- #
# 	Module:       main.py                                                      #
#   Team:         13765Y MTS_CtrlAltDefeat                                     #
# 	Author:       Chaitya Jain                                                 #
# 	Description:  Code for VRC 2024: Over Under                                #
# ---------------------------------------------------------------------------- #

from vex import *
import math

# defining stuff
brain = Brain()
controller = Controller()

right_drive_back = Motor(Ports.PORT1, True)
right_drive_front = Motor(Ports.PORT2, True)
left_drive_back = Motor(Ports.PORT10)
left_drive_front = Motor(Ports.PORT9)
left_drive_smart = MotorGroup(left_drive_back, left_drive_front)
right_drive_smart = MotorGroup(right_drive_back, right_drive_front)
drivetrain = DriveTrain(left_drive_smart, right_drive_smart, 21.56, 18, 16, INCHES)
flywheel_motor = Motor(Ports.PORT20)
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
    left_drive_smart.spin(REVERSE, (vals[0]*0.9), PERCENT)
    right_drive_smart.spin(REVERSE, (vals[1]*0.9), PERCENT)
    brain.screen.print("left: " + str(vals[0]) + "| right: " + str(vals[1]))
    brain.screen.next_row()

def stickMovement():
    vals = [getLeftInput(), getRightInput()]
    Move(vals)

#flywheel code

flywheelSpeed = 0
override = False

def flywheel():
    getFlyWheelInput()
    spinFlyWheel()
    brain.screen.print(flywheel_motor.velocity(PERCENT))

def getFlyWheelInput():
    global flywheelSpeed
    if(controller.buttonL2.pressing()):
        flywheelSpeed = 0
    elif(controller.buttonL1.pressing()):
        flywheelSpeed = 75
    elif(controller.buttonR2.pressing()):
        flywheelSpeed = 80
    elif(controller.buttonR1.pressing()):
        flywheelSpeed = 100

def spinFlyWheel():
    flywheel_smart.spin(FORWARD, flywheelSpeed, PERCENT)

brain.screen.draw_image_from_file("logo.png", 0, 0)

def autonomous():
    #auton
    brain.screen.print("starting auton")
    brain.screen.print("velocity set")
    drivetrain.drive(REVERSE, 100, PERCENT)
    wait(10, SECONDS)
    drivetrain.drive(REVERSE, 0, PERCENT)
    right_drive_smart.spin(FORWARD)
    wait(1, SECONDS)
    right_drive_smart.spin(FORWARD, 0, PERCENT)
    drivetrain.drive(REVERSE, 100, PERCENT)
    brain.screen.print("ending auton")

def usercontrol():
    global counter
    while True:
        wait(10)
        stickMovement()
        flywheel()
        counter = counter +1
        if(counter == 5):
            brain.screen.clear_screen()
            brain.screen.set_cursor(1,1)
            counter = 0

comp = Competition(usercontrol, autonomous)
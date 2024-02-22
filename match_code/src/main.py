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
wing_motor = Motor(Ports.PORT16, REVERSE)
wing_motor_smart = MotorGroup(wing_motor)
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
    #brain.screen.print("left: " + str(vals[0]) + "| right: " + str(vals[1]))
    #brain.screen.next_row()

def stickMovement():
    vals = [getLeftInput(), getRightInput()]
    if(controller.buttonA.pressing()):
        vals[0] = vals[0] * 0.5
        vals[1] = vals[1] * 0.5
    elif(controller.buttonB.pressing()):
        goUnderPoleAutonomous()
    Move(vals)

def goUnderPoleAutonomous():
    drivetrain.drive(REVERSE, 50, PERCENT)
    wait(3.4, SECONDS)
    drivetrain.drive(REVERSE, 0, PERCENT)

#flywheel code

flywheelSpeed = 0
override = False

def flywheel():
    getFlyWheelInput()
    spinFlyWheel()
    #brain.screen.print(flywheel_motor.velocity(PERCENT))

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

# flywheel PID

def PID(wantedSpeed):
    if(flywheel_smart.velocity(PERCENT) > 80):
        flywheel_smart.set_velocity((wantedSpeed-2), PERCENT)

# wing
        
wingDown = False

def wing():
    global wingDown
    if(wingDown == False):
        wing_motor_smart.spin(FORWARD, 100, PERCENT)
    elif(wingDown == True):
        wing_motor_smart.spin(REVERSE, 100, PERCENT)
    if(controller.buttonA.pressing()): 
        if(wingDown == False):
            wing_motor_smart.spin_for(REVERSE, 0.2, SECONDS, 70, PERCENT)
            wingDown = True
        elif (wingDown == True):
            wing_motor_smart.spin_for(FORWARD, 0.2, SECONDS, 50, PERCENT)
            wingDown = False

def autonomous():
    #auton
    brain.screen.draw_image_from_file('logoForBrain.bmp', 0, 0)
    brain.screen.print("starting auton")
    brain.screen.print("velocity set")
    drivetrain.drive(REVERSE, 30, PERCENT)
    wait(0.5, SECONDS)
    drivetrain.drive(REVERSE, 0, PERCENT)
    right_drive_smart.spin(FORWARD)
    wait(0.3, SECONDS)
    right_drive_smart.spin(FORWARD, 0, PERCENT)
    drivetrain.drive(FORWARD, 30, PERCENT)
    wait(0.7, SECONDS)
    drivetrain.drive(FORWARD, 0, PERCENT)
    right_drive_smart.spin_for(FORWARD, 0.5, SECONDS, 50, PERCENT)
    wait(0.5, SECONDS)
    right_drive_smart.spin(FORWARD, 0, PERCENT)
    left_drive_smart.spin(REVERSE, 15, PERCENT)
    wait(0.2, SECONDS)
    left_drive_smart.spin(REVERSE, 0, PERCENT)
    brain.screen.print("ending auton")


def usercontrol():
    global counter
    global flywheelSpeed
    flywheelSpeed = 80
    while True:
        wait(10)
        stickMovement()
        flywheel()
        wing()
        PID(flywheelSpeed)
        counter = counter +1
        if(counter == 5):
            brain.screen.clear_screen()
            brain.screen.set_cursor(1,1)
            counter = 0

comp = Competition(usercontrol, autonomous)
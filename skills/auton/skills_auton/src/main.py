# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       Chaitya Jain                                                 #
# 	Created:      1/26/2024, 2:59:12 PM                                        #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

# Brain should be defined by default
brain=Brain()
# defining stuff
brain = Brain()
controller = Controller()

right_drive_back = Motor(Ports.PORT1, True)
right_drive_front = Motor(Ports.PORT2, True)
left_drive_back = Motor(Ports.PORT10)
left_drive_front = Motor(Ports.PORT9)
left_drive_smart = MotorGroup(left_drive_back, left_drive_front)
right_drive_smart = MotorGroup(right_drive_back, right_drive_front)
drivetrain = DriveTrain(left_drive_smart, right_drive_smart)
flywheel_motor = Motor(Ports.PORT20)
flywheel_smart = MotorGroup(flywheel_motor)

#flywheel code

flywheelSpeed = 100

def flywheel():
    getFlyWheelInput()
    spinFlyWheel()
    brain.screen.print(flywheelSpeed)

def getFlyWheelInput():
    global flywheelSpeed
    if(controller.buttonUp.pressing() and flywheelSpeed < 100):
        flywheelSpeed = flywheelSpeed + 50
    elif(controller.buttonDown.pressing() and flywheelSpeed > 0):
        flywheelSpeed = flywheelSpeed - 50

def spinFlyWheel():
    flywheel_smart.spin(FORWARD, flywheelSpeed, PERCENT)

for i in range(55):
    spinFlyWheel()
    wait(1, SECONDS)
flywheelSpeed = 0
drivetrain.drive(REVERSE, 100, PERCENT)
wait(5, SECONDS)
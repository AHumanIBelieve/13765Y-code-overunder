# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
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
wing_motor_left = Motor(Ports.PORT16, REVERSE)
wing_motor_left_smart = MotorGroup(wing_motor_left)
wing_motor_right = Motor(Ports.PORT14)
wing_motor_right_smart = MotorGroup(wing_motor_right)
flywheel_motor = Motor(Ports.PORT20)
flywheel_smart = MotorGroup(flywheel_motor)

#flywheel code

flywheelSpeed = 80

def spinFlyWheel():
    flywheel_smart.spin(FORWARD, flywheelSpeed, PERCENT)

# flywheel PID

def PID(wantedSpeed):
    if(flywheel_smart.velocity(PERCENT) > 80):
        flywheel_smart.set_velocity(wantedSpeed-1)

wingDown = False

def wing():
    global wingDown
    if(wingDown == False):
        wing_motor_left_smart.spin(FORWARD, 10, PERCENT)
        wing_motor_right_smart.spin(REVERSE, 10, PERCENT)
    elif(wingDown == True):
        wing_motor_left_smart.spin(REVERSE, 70, PERCENT)
        wing_motor_right_smart.spin(FORWARD, 70, PERCENT)
        
def wingToggle():
    global wingDown
    if(wingDown == False):
        wing_motor_left_smart.spin_for(REVERSE, 0.2, SECONDS, 70, PERCENT)
        wing_motor_right_smart.spin_for(FORWARD, 0.2, SECONDS, 70, PERCENT)
        wingDown = True
    elif (wingDown == True):
        wing_motor_left_smart.spin_for(FORWARD, 0.8, SECONDS, 90, PERCENT)
        wing_motor_right_smart.spin_for(REVERSE, 0.8, SECONDS, 90, PERCENT)
        wingDown = False

def auton():
    wingToggle()
    drivetrain.drive(REVERSE, 50, PERCENT)
    wait(1, SECONDS)
    drivetrain.drive(REVERSE, 0, PERCENT)
    drivetrain.drive(FORWARD, 50, PERCENT)
    wait(1, SECONDS)
    drivetrain.drive(FORWARD, 0)
    left_drive_smart.spin_for(REVERSE, 3, SECONDS, 30, PERCENT)
    wingToggle()
    timer = 0
    while(timer<45):
        spinFlyWheel()
        wait(1, SECONDS)
        timer += 1
    drivetrain.drive(REVERSE, 50, PERCENT)
    wait(2, SECONDS)
    drivetrain.drive(REVERSE, 0)
    left_drive_smart.spin_for(REVERSE, 1, SECONDS, 80, PERCENT)
    drivetrain.drive(FORWARD, 80, PERCENT)
    wait(5, SECONDS)
    drivetrain.drive(FORWARD, 0)
    left_drive_smart.spin_for(REVERSE, 1, SECONDS, 80, PERCENT)
    wingToggle()
    drivetrain.drive(REVERSE, 100, PERCENT)

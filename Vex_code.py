#region VEXcode Generated Robot Configuration
from vex import *
import urandom
import math

# Brain should be defined by default
brain = Brain()

# Robot configuration code
brain_inertial = Inertial()

left_motor = Motor(Ports.PORT6)
right_motor = Motor(Ports.PORT10, True)
arm_motor = Motor(Ports.PORT3)
claw_motor = Motor(Ports.PORT4)

# Wait for sensor(s) to fully initialize
wait(100, MSEC)

# generating and setting random seed
def initializeRandomSeed():
    wait(100, MSEC)
    xaxis = brain_inertial.acceleration(XAXIS) * 1000
    yaxis = brain_inertial.acceleration(YAXIS) * 1000
    zaxis = brain_inertial.acceleration(ZAXIS) * 1000
    systemTime = brain.timer.system() * 100
    urandom.seed(int(xaxis + yaxis + zaxis + systemTime))

# Initialize random seed
initializeRandomSeed()

#endregion VEXcode Generated Robot Configuration

# --------------------------------
# Choose destination here
# --------------------------------
DESTINATION = "A"   # A, B, C, or D

# --------------------------------
# Screen text
# --------------------------------
def show_status(text):
    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)
    brain.screen.print(text)

# --------------------------------
# Stopping modes
# --------------------------------
def set_motor_modes():
    left_motor.set_stopping(BRAKE)
    right_motor.set_stopping(BRAKE)
    arm_motor.set_stopping(HOLD)
    claw_motor.set_stopping(HOLD)

# --------------------------------
# Drive functions
# --------------------------------
def stop_drive():
    left_motor.stop(BRAKE)
    right_motor.stop(BRAKE)

def drive_forward(time_sec, speed=35):
    left_motor.spin(FORWARD, speed, PERCENT)
    right_motor.spin(FORWARD, speed, PERCENT)
    wait(time_sec, SECONDS)
    stop_drive()

def drive_backward(time_sec, speed=35):
    left_motor.spin(REVERSE, speed, PERCENT)
    right_motor.spin(REVERSE, speed, PERCENT)
    wait(time_sec, SECONDS)
    stop_drive()

def turn_left(time_sec, speed=40):
    left_motor.spin(REVERSE, speed, PERCENT)
    right_motor.spin(FORWARD, speed, PERCENT)
    wait(time_sec, SECONDS)
    stop_drive()

def turn_right(time_sec, speed=40):
    left_motor.spin(FORWARD, speed, PERCENT)
    right_motor.spin(REVERSE, speed, PERCENT)
    wait(time_sec, SECONDS)
    stop_drive()
def return_home():
    show_status("Returning home")

    # Reverse fully back to middle/home
    drive_backward(MIDDLE_TO_BIN, 35)
    wait(0.3, SECONDS)

    # Small straighten (optional tweak if needed)
    # turn_left(0.1) or turn_right(0.1)

    show_status("At home")

# --------------------------------
# Arm and claw
# --------------------------------
def arm_up(time_sec=0.9, speed=40):
    arm_motor.spin(FORWARD, speed, PERCENT)
    wait(time_sec, SECONDS)
    arm_motor.stop(HOLD)

def arm_down(time_sec=0.9, speed=40):
    arm_motor.spin(REVERSE, speed, PERCENT)
    wait(time_sec, SECONDS)
    arm_motor.stop(HOLD)

def open_claw(time_sec=0.7, speed=40):
    claw_motor.spin(REVERSE, speed, PERCENT)
    wait(time_sec, SECONDS)
    claw_motor.stop(HOLD)

def close_claw(time_sec=1.0, speed=50):
    # Stronger close so it grips before reversing
    claw_motor.spin(FORWARD, speed, PERCENT)
    wait(time_sec, SECONDS)
    claw_motor.stop(HOLD)

# --------------------------------
# Route timings
# KEEPING YOUR DISTANCES/TIMES
# --------------------------------
START_TO_MIDDLE = 1.0
MIDDLE_TO_BIN = 2.7
HALF_RETURN = 0.5

# A = left
A_TURN_OUT = 1.55
A_TURN_BACK = 1.20
A_DRIVE = 1.35

# B = right
B_TURN_OUT = 1.05
B_TURN_BACK = 1.20
B_DRIVE = 1.35

# C = more forward and left
C_FORWARD_FIRST = 0.8
C_TURN_OUT = 0.85
C_TURN_BACK = 1.00
C_DRIVE = 1.30

# D = more forward and right
D_FORWARD_FIRST = 0.8
D_TURN_OUT = 0.85
D_TURN_BACK = 1.00
D_DRIVE = 1.30

# --------------------------------
# Start outside square -> middle
# --------------------------------
def move_into_square():
    show_status("Move to middle")
    drive_forward(START_TO_MIDDLE, 35)
    wait(0.3, SECONDS)

# --------------------------------
# Pick up bin
# --------------------------------
def collect_bin():
    show_status("Arm down")
    arm_down(0.8)
    wait(0.3, SECONDS)

    show_status("Claw open")
    open_claw(0.7)
    wait(0.3, SECONDS)

    show_status("Forward to bin")
    drive_forward(MIDDLE_TO_BIN, 35)
    wait(0.3, SECONDS)

    show_status("Close claw")
    close_claw(1.0, 50)
    wait(0.5, SECONDS)
    claw_motor.stop(HOLD)

    show_status("Lift arm")
    arm_up(0.9)
    wait(0.3, SECONDS)
    arm_motor.stop(HOLD)
    claw_motor.stop(HOLD)

    show_status("Back to middle")
    drive_backward(MIDDLE_TO_BIN, 35)
    wait(0.3, SECONDS)

# --------------------------------
# Drop bin
# --------------------------------
def drop_bin():
    show_status("Open claw")
    open_claw(0.7)
    wait(0.3, SECONDS)

    show_status("Lift arm slightly")
    arm_up(0.3)
    wait(0.2, SECONDS)

    
# --------------------------------
# Route A: left
# --------------------------------
def go_to_A():
    show_status("Turn left to A")
    turn_left(A_TURN_OUT, 40)
    wait(0.3, SECONDS)

    show_status("Drive to A")
    drive_forward(A_DRIVE, 35)
    wait(0.3, SECONDS)

    drop_bin()

    show_status("Reverse from A")
    drive_backward(A_DRIVE, 35)
    wait(0.3, SECONDS)

    show_status("Turn back")
    turn_right(A_TURN_BACK, 40)
    wait(0.3, SECONDS)

    return_home()


# --------------------------------
# Route B: right
# --------------------------------
def go_to_B():
    show_status("Turn right to B")
    turn_right(B_TURN_OUT, 40)
    wait(0.3, SECONDS)

    show_status("Drive to B")
    drive_forward(B_DRIVE, 35)
    wait(0.3, SECONDS)

    drop_bin()

    show_status("Reverse from B")
    drive_backward(B_DRIVE, 35)
    wait(0.3, SECONDS)

    show_status("Turn back")
    turn_left(B_TURN_BACK, 40)
    wait(0.3, SECONDS)

    return_home()

# --------------------------------
# Route C: more forward and left
# --------------------------------
def go_to_C():
    show_status("Forward for C")
    drive_forward(C_FORWARD_FIRST, 35)
    wait(0.3, SECONDS)

    show_status("Turn left to C")
    turn_left(C_TURN_OUT, 40)
    wait(0.3, SECONDS)

    show_status("Drive to C")
    drive_forward(C_DRIVE, 35)
    wait(0.3, SECONDS)

    drop_bin()

    show_status("Reverse from C")
    drive_backward(C_DRIVE, 35)
    wait(0.3, SECONDS)

    show_status("Turn back")
    turn_right(C_TURN_BACK, 40)
    wait(0.3, SECONDS)

    show_status("Reverse to middle")
    drive_backward(C_FORWARD_FIRST, 35)
    wait(0.3, SECONDS)

    return_home()

# --------------------------------
# Route D: more forward and right
# --------------------------------
def go_to_D():
    show_status("Forward for D")
    drive_forward(D_FORWARD_FIRST, 35)
    wait(0.3, SECONDS)

    show_status("Turn right to D")
    turn_right(D_TURN_OUT, 40)
    wait(0.3, SECONDS)

    show_status("Drive to D")
    drive_forward(D_DRIVE, 35)
    wait(0.3, SECONDS)

    drop_bin()

    show_status("Reverse from D")
    drive_backward(D_DRIVE, 35)
    wait(0.3, SECONDS)

    show_status("Turn back")
    turn_left(D_TURN_BACK, 40)
    wait(0.3, SECONDS)

    show_status("Reverse to middle")
    drive_backward(D_FORWARD_FIRST, 35)
    wait(0.3, SECONDS)

    return_home()

# --------------------------------
# Main
# --------------------------------
def main():
    set_motor_modes()

    show_status("Starting")
    wait(1, SECONDS)

    move_into_square()
    collect_bin()

    if DESTINATION == "A":
        go_to_A()
    elif DESTINATION == "B":
        go_to_B()
    elif DESTINATION == "C":
        go_to_C()
    elif DESTINATION == "D":
        go_to_D()
    else:
        show_status("Invalid route")
        return

    show_status("Finished")
    arm_motor.stop(HOLD)
    claw_motor.stop(HOLD)

main()

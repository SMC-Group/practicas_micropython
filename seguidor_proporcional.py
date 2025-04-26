#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase

# Initialize the motors and the drive base
# Adjust the ports if you connected your motors to different ports
left_motor = Motor(Port.A)
right_motor = Motor(Port.D, Direction.COUNTERCLOCKWISE)

# Initialize the Color Sensor
# Adjust the port if you connected your sensor to a different port
line_sensor = ColorSensor(Port.S2)

# Initialize the DriveBase.
# Measure the wheel diameter and axle track of your robot and update these values.
# Wheel diameter is the diameter of your wheels in millimeters.
# Axle track is the distance between the centers of the two wheels in millimeters.
robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=114)

# --- Calibration ---
# It's highly recommended to calibrate your sensor for the specific
# surface and line you are using.
# You can uncomment the calibration section below and run it first
# to get the black and white values, then update the BLACK and WHITE variables.

# print("Place sensor on WHITE and press center button.")
# while not ev3.buttons.pressed(Button.CENTER):
#     wait(10)
# white_value = line_sensor.reflection()
# print("White value:", white_value)

# print("Place sensor on BLACK and press center button.")
# while not ev3.buttons.pressed(Button.CENTER):
#     wait(10)
# black_value = line_sensor.reflection()
# print("Black value:", black_value)

# print("Update BLACK and WHITE variables in the code with these values.")
# exit() # Exit after calibration


# Define the reflected light values for black and white.
# You should get these values by calibrating your sensor on your track.
BLACK = 23
WHITE = 100

# Calculate the threshold value. This is the target sensor reading.
threshold = (BLACK + WHITE) / 2

# Set the desired forward speed for the robot (in mm/s)
DRIVE_SPEED = 100

# Set the proportional gain (Kp). This value determines how strongly the
# robot reacts to the error. You will likely need to tune this value
# for your specific robot and track.
# Start with a small value (e.g., 0.5) and increase it gradually if needed.
PROPORTIONAL_GAIN = 1.2 # Example value, tune this!

robot.reset()
# --- Line Following Loop ---
print("Starting line following. Press any button to stop.")

while robot.distance() < (30 * 10):
    # Read the reflected light intensity
    reflection = line_sensor.reflection()

    # Calculate the error: difference between the sensor reading and the threshold
    # If the sensor is on white (value > threshold), error is positive.
    # If the sensor is on black (value < threshold), error is negative.
    error = reflection - threshold

    # Calculate the turn rate using the proportional control law
    # turn_rate = Kp * error
    turn_rate = PROPORTIONAL_GAIN * error

    # Control the robot's movement
    # The robot will drive forward at DRIVE_SPEED and turn with turn_rate
    robot.drive(DRIVE_SPEED, turn_rate)

    # Optional: Add a small wait to avoid reading the sensor too fast
    # wait(10)

    # Check for a button press to stop the program
    # You might need to import Button from pybricks.parameters and ev3 from pybricks.hubs
    # if you want to use button presses for stopping. For simplicity,
    # you can stop the program manually in your MicroPython environment.
    # if ev3.buttons.any():
    #     break

# print("Line following stopped.")
# robot.stop(Stop.BRAKE)
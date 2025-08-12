#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import ColorSensor, Motor
from pybricks.parameters import Port, Direction, Button
from pybricks.tools import wait
from umake.umake_robot import Robot, TurnLeft, TurnRight
from umake.median_motor import UmakeMedianMotor
from umake.line_followers import LineFollowers, LineSideLeft

WHEEL_DIAMETER = 62
motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
second_motor = Motor(Port.C)
medium_motor = UmakeMedianMotor(Port.D, WHEEL_DIAMETER)
left_color_sensor = ColorSensor(Port.S2)
right_color_sensor = ColorSensor(Port.S3)
robot = Robot(motor, second_motor, WHEEL_DIAMETER, 175)
line_followers = LineFollowers(robot, right_color_sensor, 35.5, left_color_sensor, 12)
hub = EV3Brick()

def wait_until_button_pressed():
    while Button.CENTER not in hub.buttons.pressed():
        wait(10)

def banderas():
    robot.run_cm(80, 30)
    robot.rotate(-90, 50)
    robot.run_cm(80, 46)
    medium_motor.safely_run_angle(-100, 800)
    medium_motor.reset_angle(0)
    wait(150)
    medium_motor.safely_run_angle(100, 500)
    robot.run_cm(-80, 5)
    robot.rotate(90, 80)
    robot.run_cm(80, 40)
    robot.rotate(90, 80)
    robot.run_by_seconds(-100,  2)
    robot.run_cm(50, 2)
    robot.rotate(90, 80)
    robot.run_cm(50, 2)
    medium_motor.safely_run_angle(-80, 255)
    robot.rotate(-45, 50)
    robot.rotate(-45, 50) 
    robot.run_by_seconds(-80, 1)
    robot.run_cm(80, 20)
    robot.rotate(45, 80)
    robot.run_cm(80, 40)
    robot.rotate(142, 80)
    robot.run_by_seconds(-80, 2)

def AB():
    robot.run_cm(80, 14)
    robot.turn(92, 80, TurnLeft)
    medium_motor.safely_run_angle(-80, 130)
    robot.run_cm(85, 25)
    robot.turn(-20, 90, TurnRight)
    robot.turn(20, 90, TurnRight)
    robot.run_cm(80, 45)
    robot.rotate(-90, 80)
    robot.run_by_seconds(-80, 1)
    robot.run_cm(80, 10.5)
    robot.rotate(90, 80)

def antenas():
    line_followers.follow_line_by_pid_until_black(50, 0.25, 0.01, 0.3, LineSideLeft)    
    # medium_motor.safely_run_by_seconds(80, 2)
wait_until_button_pressed()
banderas()
AB()
antenas()
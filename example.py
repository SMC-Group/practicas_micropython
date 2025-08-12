#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import ColorSensor, Motor
from pybricks.parameters import Port, Direction
from pybricks.tools import wait
from umake.umake_robot import Robot, TurnLeft, TurnRight
from umake.median_motor import UmakeMedianMotor

WHEEL_DIAMETER = 62
motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
second_motor = Motor(Port.C)
medium_motor = UmakeMedianMotor(Port.D, WHEEL_DIAMETER)
left_color_sensor = ColorSensor(Port.S2)
right_color_sensor = ColorSensor(Port.S3)
robot = Robot(motor, second_motor, WHEEL_DIAMETER, 175)

def banderas():
    robot.run_cm(80, 30)
    robot.rotate(-90, 50)
    # robot.run_by_seconds(-90, 2)
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
    robot.run_cm(80, 15)
    robot.turn(92, 80, TurnLeft)
    medium_motor.safely_run_angle(-80, 120)
    robot.run_cm(80, 25)
    robot.turn(-20, 80, TurnRight)
    robot.turn(20, 80, TurnRight)
    robot.run_cm(80, 40)
    robot.rotate(-90, 80)
    robot.run_by_seconds(-80, 1)
    robot.run_cm(80, 12.5)

banderas()
AB()
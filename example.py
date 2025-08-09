#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import ColorSensor, Motor
from pybricks.parameters import Port, Direction
from pybricks.tools import wait
from umake.umake_robot import Robot
from umake.median_motor import UmakeMedianMotor

WHEEL_DIAMETER = 62
motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
second_motor = Motor(Port.C)
medium_motor = UmakeMedianMotor(Port.D, WHEEL_DIAMETER)
left_color_sensor = ColorSensor(Port.S2)
right_color_sensor = ColorSensor(Port.S3)
robot = Robot(motor, second_motor, WHEEL_DIAMETER, 175)

def banderas():
    robot.run_cm(50, 30)
    robot.rotate(-90)
    robot.run_by_seconds(-90, 2)
    robot.run_cm(50, 58)
    medium_motor.safely_run_angle(-100, 800)
    medium_motor.reset_angle(0)
    wait(150)
    medium_motor.safely_run_angle(100, 500)
    # TODO: revisar giro
    robot.turn(-45, 50)
    robot.rotate(90)
    robot.run_cm(75, 40)
    robot.reset_motors()
    robot.rotate(90)
    robot.run_by_seconds(-50, 2)
    robot.run_cm(50, 15)
    # TODO: revisar instrucción
    robot.run_cm(-25, 90)
    robot.run_cm(50, 25)
    # TODO: revisar instrucción
    robot.run_cm(25, 90)
    # TODO: faltan dos instrucciones

banderas()
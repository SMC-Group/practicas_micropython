#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Direction
from umake.umake_robot import Robot

left_motor = Motor(Port.A)
right_motor = Motor(Port.D, Direction.COUNTERCLOCKWISE)
robot = Robot(left_motor, right_motor, 62, 175)

robot.turn(90, 50)
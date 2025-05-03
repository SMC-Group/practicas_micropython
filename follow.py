#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Direction
from umake.umake_robot import Robot
from umake.line_followers import LineFollowers

left_motor = Motor(Port.A, Direction.CLOCKWISE)
right_motor = Motor(Port.D, Direction.COUNTERCLOCKWISE)

robot = Robot(left_motor, right_motor, 62, 175)

# Cambiar puerto del sensor de color
left_color_sensor = ColorSensor(Port.S2)
# Poner media
line_follower = LineFollowers(robot, left_color_sensor, (23 + 100) / 2)
line_follower.follow_line_by_pid(50, 1.2, 0.001, 1, 90)
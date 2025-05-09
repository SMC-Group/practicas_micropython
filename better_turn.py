#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Direction
from umake.umake_robot import Robot
from umake.line_followers import LineFollowers

left_motor = Motor(Port.A, Direction.CLOCKWISE)
right_motor = Motor(Port.D, Direction.COUNTERCLOCKWISE)
left_color_sensor = ColorSensor(Port.S2)
right_color_sensor = ColorSensor(Port.S4)

robot = Robot(left_motor, right_motor, 62, 175, 8)
line_follower = LineFollowers(robot, right_color_sensor, (23 + 100) / 2, left_color_sensor, 30)
line_follower.follow_line_by_pid(50, 0.7, 0.001, 1, 30)
robot.run_cm(50, 9)
robot.rotate(90, 50)

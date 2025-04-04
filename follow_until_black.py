#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import ColorSensor, Motor
from pybricks.parameters import Direction, Port
from umake.umake_robot import Robot
from umake.line_followers import LineFollowers

left_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.C, Direction.CLOCKWISE)
median_motor = Motor(Port.D)
color_sensor = ColorSensor(Port.S3)
second_color_sensor = ColorSensor(Port.S2)

robot = Robot(left_motor, right_motor, 62, 175)
line_follower = LineFollowers(robot, color_sensor, (11 + 57) / 2, second_color_sensor, 20)
line_follower.follow_line_by_pid_until_black(50, 0.35, 0.001, 2.5)
robot.run_cm(80, 9)
robot.turn(90, 50)
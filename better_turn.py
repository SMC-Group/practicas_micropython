#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Direction
from umake.umake_robot import Robot
from umake.line_followers import LineFollowers, LineSideLeft

left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.C)
left_color_sensor = ColorSensor(Port.S2)
right_color_sensor = ColorSensor(Port.S3)
robot = Robot(left_motor, right_motor, 62, 175, 8)
line_follower = LineFollowers(robot, right_color_sensor, (9 + 57) / 2, left_color_sensor, 14)
line_follower.follow_line_by_pid_until_black(30, 0.1, 0.01, 0.3, LineSideLeft)
robot.run_cm(50, 9)
robot.rotate(90, 50)

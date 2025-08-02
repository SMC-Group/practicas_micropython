#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import ColorSensor, Motor
from pybricks.parameters import Port, Direction
# from umake.line_followers import LineFollowers, LineSideLeft
from umake.umake_robot import Robot, TurnLeft

motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
second_motor = Motor(Port.C)
left_color_sensor = ColorSensor(Port.S2)
right_color_sensor = ColorSensor(Port.S3)
robot = Robot(motor, second_motor, 62, 175)
robot.run_cm(50, 100)
robot.rotate(90, 50)
robot.run_cm(50, 15)
# line_follower = LineFollowers(robot, left_color_sensor, (25 + 10) / 2, right_color_sensor, 10)
# line_follower.follow_line_by_pid_until_black(30, 0.1, 0.01, 0.3, LineSideLeft)
#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import ColorSensor, Motor
from pybricks.parameters import Direction, Port
from umake.umake_robot import Robot
from umake.line_followers import LineFollowers

left_motor = Motor(Port.A)
right_motor = Motor(Port.D, Direction.COUNTERCLOCKWISE)
color_sensor = ColorSensor(Port.S4)
second_color_sensor = ColorSensor(Port.S2)

robot = Robot(left_motor, right_motor, 62, 175)
line_follower = LineFollowers(robot, color_sensor, (25 + 100) / 2, second_color_sensor, 20)
line_follower.follow_line_by_pid_until_black(speed=50, Kp=1.2, Ki=0.001, Kd=1)
robot.rotate(90, 50)

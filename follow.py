#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Direction
from umake.umake_robot import Robot
from umake.line_followers import LineFollowers, LineSideLeft

left_motor = Motor(Port.D, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.A, Direction.CLOCKWISE)

robot = Robot(left_motor, right_motor, 62, 195)
 
left_color_sensor = ColorSensor(Port.S4)
# Poner medial
line_follower = LineFollowers(robot, left_color_sensor, (26 + 100) / 2)
# line_follower.follow_line_by_pid(80, 0.7, 0.001, 3, 105, LineSideLeft)
robot.turn(-90, 50)
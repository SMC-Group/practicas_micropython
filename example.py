#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import ColorSensor, Motor
from pybricks.parameters import Port, Direction, Button
from pybricks.tools import wait
from umake.umake_robot import Robot, TurnLeft, TurnRight
from umake.median_motor import UmakeMedianMotor
from umake.line_followers import LineFollowers, LineSideLeft, LineSideRight

WHEEL_DIAMETER = 62
motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
second_motor = Motor(Port.C)
medium_motor = UmakeMedianMotor(Port.D, WHEEL_DIAMETER)
direction_medium_motor = UmakeMedianMotor(Port.A, WHEEL_DIAMETER)
left_color_sensor = ColorSensor(Port.S2)
right_color_sensor = ColorSensor(Port.S3)
square_color_sensor = ColorSensor(Port.S1)
robot = Robot(motor, second_motor, WHEEL_DIAMETER, 175)
line_followers = LineFollowers(robot, left_color_sensor, 35.5, right_color_sensor, 12)
inverted_line_followers = LineFollowers(robot, right_color_sensor, 35.5, left_color_sensor, 12)
hub = EV3Brick()
global color

def read_sensor():
    color = square_color_sensor.color()
    hub.screen.print(color)

def wait_until_button_pressed():
    while Button.CENTER not in hub.buttons.pressed():
        wait(10)

def banderas():
    medium_motor.safely_run_by_seconds(100, 1)
    direction_medium_motor.safely_run_angle(50, 90)
    robot.run_cm(80, 30)
    robot.rotate(-90, 50)
    robot.run_cm(80, 46)
    medium_motor.safely_run_angle(-100, 850)
    medium_motor.reset_angle(0)
    wait(150)
    medium_motor.safely_run_angle(100, 500)
    robot.run_cm(-80, 5)
    robot.rotate(90, 80)
    robot.run_cm(80, 41)
    robot.rotate(90, 80)
    robot.run_cm(45, 5)
    wait(1000)
    read_sensor()

def segunda_funcion_banderas():
    robot.run_by_seconds(-100,  1)
    robot.run_cm(50, 2)
    robot.rotate(90, 80)
    robot.run_cm(50, 2)
    medium_motor.safely_run_angle(-80, 250)
    robot.rotate(-45, 50)
    robot.rotate(-45, 50)
    robot.run_by_seconds(-80, 1)
    robot.run_cm(80, 20)
    robot.rotate(45, 80)
    robot.run_cm(80, 40)
    robot.rotate(142, 80)
    robot.run_by_seconds(-80, 2)

def AB():
    robot.run_cm(80, 19)
    robot.turn(92, 80, TurnLeft)
    medium_motor.safely_run_by_seconds(-80, 0.5)
    robot.run_cm(85, 28)
    robot.turn(-25, 90, TurnRight)
    robot.turn(25, 90, TurnRight)
    robot.run_cm(80, 50)
    robot.rotate(-90, 80)

def primera_antena():
    robot.run_by_seconds(-80, 1)
    medium_motor.safely_run_by_seconds(100, 2)
    robot.run_cm(80, 12.5)
    robot.rotate(90, 80)
    inverted_line_followers.follow_line_by_pid_until_black(50, 0.3, 0.01, 0.3, LineSideLeft)
    inverted_line_followers.follow_line_by_pid(50, 0.3, 0.01, 0.3, 11, LineSideLeft)
    robot.run_cm(80, 13)
    medium_motor.safely_run_angle(-100, 250)
    robot.rotate(-90, 30)
    robot.run_cm(80, 65)
    robot.rotate(45, 80)
    robot.run_cm(80, 6)
    medium_motor.safely_run_angle(100, 250)
    robot.run_cm(80, -70)
    robot.rotate(-45, 80)

def deslizar_roja():
    robot.run_cm(80, 10)
    medium_motor.safely_run_angle(-100, 700)
    robot.run_cm(80, -10)
    medium_motor.safely_run_angle(100, 700)

def antena_amarilla():
    robot.run_by_seconds(-80, 2)
    medium_motor.safely_run_by_seconds(100, 2)
    robot.run_cm(80, 12.5)
    robot.rotate(90, 80)
    inverted_line_followers.follow_line_by_pid_until_black(50, 0.3, 0.01, 0.3, LineSideLeft)
    inverted_line_followers.follow_line_by_pid(50, 0.3, 0.01, 0.3, 11, LineSideLeft)
    robot.run_cm(80, 24)
    medium_motor.safely_run_angle(-100, 250)
    robot.rotate(90, 30)
    robot.run_cm(80, -40)
    robot.rotate(-55, 80)
    robot.run_cm(80, -10)
    medium_motor.safely_run_angle(100, 250)
    robot.run_cm(80, -10)

def cubo():
    robot.turn(-135, 80, TurnLeft)
    robot.run_by_seconds(-80, 2)
    robot.run_cm(80, 12.5)
    robot.rotate(-90, 80)

def segunda_funcion_cubo():
    line_followers.follow_line_by_pid_until_black(100, 0.3, 0.01, 0.3, LineSideRight)
    line_followers.follow_line_by_pid(100, 0.3, 0.01, 0.3, 95, LineSideRight)
    robot.run_cm(80, 25)
    robot.rotate(90, 80)
    robot.run_by_seconds(-80, 1)
    robot.run_cm(80, 20)
    medium_motor.safely_run_by_seconds(-80, 1.77)
    robot.run_cm(80, 35.5)
    robot.rotate(95, 80)
    robot.run_cm(80, 55)

wait_until_button_pressed()
# banderas()
# segunda_funcion_banderas()
# AB()
# primera_antena()
# deslizar_roja()
# antena_amarilla()
# cubo()
segunda_funcion_cubo()
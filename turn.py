#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Direction
from pybricks.tools import wait
from pybricks.robotics import DriveBase

left_motor = Motor(Port.A)
right_motor = Motor(Port.D, Direction.COUNTERCLOCKWISE)
line_sensor = ColorSensor(Port.S2)

robot = DriveBase(left_motor, right_motor, wheel_diameter=62, axle_track=175)

BLACK = 23
WHITE = 100
threshold = (BLACK + WHITE) / 2

def seguidor_pid(media: float, potencia: float, distancia: float, Kp: float, Ki: float, Kd: float):
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)

    error = 0
    integral = 0
    derivative = 0
    lastError = 0
    robot.stop()
    left_motor.brake()
    right_motor.brake()

    while robot.distance() <= distancia:
        error = (line_sensor.reflection() - media) * Kp
        integral = (integral + error) * Ki
        derivative = (error - lastError) * Kd
        
        correccion = error + integral + derivative
        lastError = error
        
        robot.drive(potencia, correccion)
        wait(10)
    
    robot.stop()
    left_motor.brake()
    right_motor.brake()

robot.settings(
    turn_rate=500,
    turn_acceleration=100,
    straight_acceleration=100
)
robot.turn(95)
robot.stop()
left_motor.brake()
right_motor.brake()
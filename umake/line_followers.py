#!/usr/bin/env pybricks-micropython
import sys
sys.path.append('/home/robot/practicas_micropython/umake')
from umake_robot import Robot
from pybricks.ev3devices import ColorSensor
from pybricks.tools import wait

class LineFollowers:
    def __init__(self, robot: Robot, color_sensor: ColorSensor, threshold: float, second_color_sensor: ColorSensor = None, black_value: float = None) -> None:
        self.robot = robot
        self.color_sensor = color_sensor
        self.second_color_sensor = second_color_sensor or None
        self.threshold = threshold
        self.black_value = black_value
    def follow_line_by_pid_forever(self, speed: float, Kp: float, Ki: float, Kd: float):
        robot = self.get_robot()
        drive_base = robot.get_drive_base()
        color_sensor = self.get_color_sensor()
        threshold = self.get_threshold()

        integral = 0
        derivative = 0
        last_error = 0
        drive_base.reset()
        while True:
            error = color_sensor.reflection() - threshold
            integral = integral + error
            derivative = error - last_error

            turn_rate = Kp * error + Ki * integral + Kd * derivative
            drive_base.drive(speed, turn_rate)
            last_error = error
            wait(10)
    def follow_line_by_pid(self, speed: float, Kp: float, Ki: float, Kd: float, distance: float):
        robot = self.get_robot()
        drive_base = robot.get_drive_base()
        left_motor = robot.get_left_motor()
        right_motor = robot.get_right_motor()
        color_sensor = self.get_color_sensor()
        threshold = self.get_threshold()

        integral = 0
        derivative = 0
        last_error = 0
        drive_base.reset()
        while drive_base.distance() <= (distance * 10):
            error = color_sensor.reflection() - threshold
            integral = integral + error
            derivative = error - last_error

            turn_rate = Kp * error + Ki * integral + Kd * derivative
            drive_base.drive(speed, turn_rate)
            last_error = error
            wait(10)
        drive_base.stop()
        left_motor.brake()
        right_motor.brake()
    def follow_line_by_pid_until_black(self, speed: float, Kp: float, Ki: float, Kd: float):
        robot = self.get_robot()
        drive_base = robot.get_drive_base()
        color_sensor = self.get_color_sensor()
        left_motor = robot.get_left_motor()
        right_motor = robot.get_right_motor()
        second_color_sensor = self.get_second_color_sensor()
        black_value = self.get_black_value()
        if not second_color_sensor:
            raise ValueError("Second color sensor is not defined")
        if not black_value:
            raise ValueError("Black value is not defined")
        threshold = self.get_threshold()

        integral = 0
        derivative = 0
        last_error = 0
        drive_base.reset()
        while second_color_sensor.reflection() >= black_value:
            error = color_sensor.reflection() - threshold
            integral = integral + error
            derivative = error - last_error

            turn_rate = Kp * error + Ki * integral + Kd * derivative
            drive_base.drive(speed, turn_rate)
            last_error = error
            wait(10)
        drive_base.stop()
        left_motor.brake()
        right_motor.brake()
    def get_robot(self) -> Robot:
        return self.robot
    def get_color_sensor(self) -> ColorSensor:
        return self.color_sensor
    def get_second_color_sensor(self) -> ColorSensor:
        return self.second_color_sensor
    def get_threshold(self) -> float:
        return self.threshold
    def get_black_value(self) -> float:
        return self.black_value
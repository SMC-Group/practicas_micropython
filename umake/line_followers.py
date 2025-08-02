#!/usr/bin/env pybricks-micropython
import sys
sys.path.append('/home/robot/practicas_micropython/umake')
from umake_robot import Robot
from pybricks.ev3devices import ColorSensor
from pybricks.tools import wait

LineSideRight = 0
LineSideLeft = 1


class LineFollowers:
    def __init__(self, robot: Robot, color_sensor: ColorSensor, threshold: float, second_color_sensor: ColorSensor = None, until_pid_value: float = None) -> None:
        self.robot = robot
        self.color_sensor = color_sensor
        self.second_color_sensor = second_color_sensor or None
        self.threshold = threshold
        self.until_pid_value = until_pid_value
    # TODO: implementar esto dentro del método en sí
    def __pid__controller__(self, target: float, current: float, Kp: float, Ki: float, Kd: float, integral_sum: float) -> float:
        internal_ki = Ki
        error_b = target - current
        internal_ki = (Ki * integral_sum) + error_b
        last_error = error_b - last_error
        
    def follow_line_by_pid_forever(self, speed: float, Kp: float, Ki: float, Kd: float):
        robot = self.get_robot()
        drive_base = robot.get_drive_base()
        color_sensor = self.get_color_sensor()
        threshold = self.get_threshold()
        max_speed = robot.get_max_speed()

        integral = 0.0
        last_error = 0.0
        drive_base.reset()
        while True:
            reflection = color_sensor.reflection()
            error = float(reflection) - float(threshold)
            integral += error
            derivative = error - last_error
            turn_rate = (Kp * error) + (Ki * integral) + (Kd * derivative)
            drive_base.drive(max_speed * (speed / 100.0), turn_rate)
            last_error = error
            wait(10)

    def follow_line_by_pid(self, speed: float, Kp: float, Ki: float, Kd: float, distance: float, line_side: int = LineSideRight):
        robot = self.get_robot()
        drive_base = robot.get_drive_base()
        left_motor = robot.get_left_motor()
        right_motor = robot.get_right_motor()
        color_sensor = self.get_color_sensor()
        threshold = self.get_threshold()
        max_speed = robot.get_max_speed()

        integral = 0.0
        last_error = 0.0
        drive_base.reset()
        while drive_base.distance() <= (distance * 10):
            reflection = color_sensor.reflection()
            error = 0
            if line_side == LineSideRight:
                error = float(reflection) - float(threshold)
            elif line_side == LineSideLeft:
                error = float(threshold) - float(reflection)
            else:
                raise ValueError("line_side param is not valid")
            integral += error
            derivative = error - last_error
            turn_rate = (Kp * error) + (Ki * integral) + (Kd * derivative)
            drive_base.drive(max_speed * (speed / 100.0), turn_rate)
            last_error = error
            wait(10)
        drive_base.stop()
        left_motor.brake()
        right_motor.brake()

    def follow_line_by_pid_until_black(self, speed: float, Kp: float, Ki: float, Kd: float, line_side: int = LineSideRight):
        robot = self.get_robot()
        drive_base = robot.get_drive_base()
        color_sensor = self.get_color_sensor()
        left_motor = robot.get_left_motor()
        right_motor = robot.get_right_motor()
        second_color_sensor = self.get_second_color_sensor()
        until_pid_value = self.get_until_pid_value()
        max_speed = robot.get_max_speed()
        if not second_color_sensor:
            raise ValueError("Second color sensor is not defined")
        if not until_pid_value:
            raise ValueError("Until PID value is not defined")
        threshold = self.get_threshold()

        integral = 0.0
        last_error = 0.0
        drive_base.reset()
        reflection_value = second_color_sensor.reflection()
        while reflection_value > until_pid_value:
            reflection = color_sensor.reflection()
            error = 0
            if line_side == LineSideRight:
                error = float(reflection) - float(threshold)
            elif line_side == LineSideLeft:
                error = float(threshold) - float(reflection)
            else:
                raise ValueError("line_side param is not valid")
            integral += error
            derivative = error - last_error
            turn_rate = (Kp * error) + (Ki * integral) + (Kd * derivative)
            drive_base.drive(max_speed * (speed / 100.0), turn_rate)
            last_error = error
            wait(10)
            reflection_value = second_color_sensor.reflection()
        drive_base.stop()
        left_motor.brake()
        right_motor.brake()

    def follow_p(self, speed: float, Kp: float, distance: float):
        """Follows a line using a proportional controller for a specific distance."""
        robot = self.get_robot()
        drive_base = robot.get_drive_base()
        left_motor = robot.get_left_motor()
        right_motor = robot.get_right_motor()
        color_sensor = self.get_color_sensor()
        threshold = self.get_threshold()
        max_speed = robot.get_max_speed()

        drive_base.reset()
        while drive_base.distance() <= (distance * 10):
            error = color_sensor.reflection() - threshold
            turn_rate = Kp * error
            drive_base.drive(max_speed * (speed / 100), turn_rate)
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

    def get_until_pid_value(self) -> float:
        return self.until_pid_value
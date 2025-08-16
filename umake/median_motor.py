#!/usr/bin/env pybricks-micropython
import sys
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Direction
from pybricks.tools import wait
sys.path.append('/home/robot/practicas_micropython/umake')

class UmakeMedianMotor(Motor):
    def __init__(self, port: Port, wheel_diameter: float, positive_direction: Direction = Direction.CLOCKWISE, gears: Union[List[int], List[List[int]]] = None):
        super().__init__(port, positive_direction, gears)
        self.wheel_diameter = wheel_diameter
        self.max_speed = (1050 / 360) * (3.1416 * self.wheel_diameter)
    def safely_run_angle(self, speed: float, angle: int):
        self.run_angle(self.max_speed * (speed / 100), angle)
        self.brake()
    def safely_run_by_seconds(self, speed: float, seconds: float):
        self.run_time(self.max_speed * (speed / 100), seconds * 1000)
        self.brake()

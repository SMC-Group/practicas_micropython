from pybricks.ev3devices import Motor
from pybricks.robotics import DriveBase

class Robot:
    def __init__(self, left_motor: Motor, right_motor: Motor, wheel_diameter: float, axle_track: float) -> None:
        self.drive_base = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)
        self.left_motor = left_motor
        self.right_motor = right_motor
    def turn(self, angle: float, speed: float = None, acceleration: float = None) -> None:
        drive_base = self.get_drive_base()
        left_motor = self.get_left_motor()
        right_motor = self.get_right_motor()
        drive_base.reset()
        if speed is not None:
            drive_base.settings(
                turn_rate=speed
            )
        if acceleration is not None:
            drive_base.settings(
                turn_acceleration=acceleration
            )
        drive_base.turn(angle)
        drive_base.stop()
        left_motor.brake()
        right_motor.brake()
    def run_cm(self, speed: float, distance: float):
        drive_base = self.get_drive_base()
        left_motor = self.get_left_motor()
        right_motor = self.get_right_motor()
        drive_base.settings(
            straight_speed=speed
        )
        drive_base.straight(distance * 10)
        drive_base.stop()
        left_motor.brake()
        right_motor.brake()
    def get_drive_base(self) -> DriveBase:
        return self.drive_base
    def get_left_motor(self) -> Motor:
        return self.left_motor
    def get_right_motor(self) -> Motor:
        return self.right_motor
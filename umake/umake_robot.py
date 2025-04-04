from pybricks.ev3devices import Motor
from pybricks.robotics import DriveBase

class Robot:
    def __init__(self, left_motor: Motor, right_motor: Motor, wheel_diameter: float, axle_track: float) -> None:
        self.drive_base = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)
        self.left_motor = left_motor
        self.right_motor = right_motor
        self.max_speed = (1050 / 360) * (3.1416 * wheel_diameter)
    def turn(self, angle: float, speed: float = None, acceleration: float = None) -> None:
        drive_base = self.get_drive_base()
        left_motor = self.get_left_motor()
        right_motor = self.get_right_motor()
        new_speed = self.get_max_speed() * (speed / 100)
        drive_base.reset()
        drive_base.settings(
            turn_rate=new_speed,
            turn_acceleration=acceleration
        )
        drive_base.turn(angle)
        drive_base.stop()
        left_motor.brake()
        right_motor.brake()
    def run_cm(self, speed: float, distance: float, straight_acceleration: float = None):
        drive_base = self.get_drive_base()
        left_motor = self.get_left_motor()
        right_motor = self.get_right_motor()
        new_speed = self.get_max_speed() * (speed / 100)
        drive_base.settings(
            straight_speed=new_speed,
            straight_acceleration=straight_acceleration
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
    def get_max_speed(self) -> float:
        return self.max_speed
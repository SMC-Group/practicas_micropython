from pybricks.ev3devices import Motor
from pybricks.robotics import DriveBase
# TODO: Hacer método turn()

class Robot:
    def __init__(self, left_motor: Motor, right_motor: Motor, wheel_diameter: float, axle_track: float, degrees_error: float = 0) -> None:
        self.drive_base = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)
        self.left_motor = left_motor
        self.right_motor = right_motor
        self.max_speed = (1050 / 360) * (3.1416 * wheel_diameter)
        self.axle_track = axle_track
        self.wheel_diameter = wheel_diameter
        self.degrees_error = degrees_error
    def rotate(self, angle: float, speed: float = None, acceleration: float = None) -> None:
        drive_base = self.get_drive_base()
        left_motor = self.get_left_motor()
        right_motor = self.get_right_motor()
        error = self.get_degrees_error()
        new_speed = self.get_max_speed() * (speed / 100)
        drive_base.reset()
        old = drive_base.settings()
        drive_base.settings(
            turn_rate=new_speed,
            turn_acceleration=acceleration
        )
        drive_base.turn(angle + error)
        drive_base.stop()
        left_motor.brake()
        right_motor.brake()
        drive_base.settings(
            turn_rate=old[2],
            turn_acceleration=old[3]
        )
    def turn(self, degrees: float, speed: float) -> None:
        left_motor = self.get_left_motor()
        right_motor = self.get_right_motor()
        max_speed = self.get_max_speed()

        if degrees > 0:
            left_motor.run_angle((max_speed * (speed / 100)) * -1, degrees)
            left_motor.brake()
        else:
            right_motor.run_angle((max_speed * (speed / 100)) * -1, degrees)
            right_motor.brake()
    def run_cm(self, speed: float, distance: float, straight_acceleration: float = None):
        drive_base = self.get_drive_base()
        left_motor = self.get_left_motor()
        right_motor = self.get_right_motor()
        new_speed = self.get_max_speed() * (speed / 100)
        old = drive_base.settings()
        drive_base.settings(
            straight_speed=new_speed,
            straight_acceleration=straight_acceleration
        )
        drive_base.straight(distance * 10)
        drive_base.stop()
        left_motor.brake()
        right_motor.brake()
        drive_base.settings(
            straight_speed=old[0],
            straight_acceleration=old[1]
        )
    def get_drive_base(self) -> DriveBase:
        return self.drive_base
    def get_left_motor(self) -> Motor:
        return self.left_motor
    def get_right_motor(self) -> Motor:
        return self.right_motor
    def get_max_speed(self) -> float:
        return self.max_speed
    def get_axle_track(self) -> float:
        return self.axle_track
    def get_wheel_diameter(self) -> float:
        return self.wheel_diameter
    def get_degrees_error(self) -> float:
        return self.degrees_error
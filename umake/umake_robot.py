from pybricks.ev3devices import ColorSensor, Motor
from pybricks.robotics import DriveBase
from pybricks.tools import wait
# TODO: Hacer método turn()

TurnLeft = 0
TurnRight = 1

# Robot()
class Robot:
    def __init__(self, left_motor: Motor, right_motor: Motor, wheel_diameter: float, axle_track: float) -> None:
        self.drive_base = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)
        self.left_motor = left_motor
        self.right_motor = right_motor
        self.max_speed = (1050 / 360) * (3.1416 * wheel_diameter)
        self.axle_track = axle_track
        self.wheel_diameter = wheel_diameter
        self.degrees_error = 0
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
    def turn(self, degrees: float, speed: float, single_motor: int):
        left_motor = self.get_left_motor()
        right_motor = self.get_right_motor()
        max_speed = self.get_max_speed()
        axle_track = self.get_axle_track()
        wheel_diameter = self.get_wheel_diameter()
        
        if single_motor != None:
            # Giro con un solo motor (el otro permanece estático)
            # El ángulo de giro es el doble porque solo un motor se mueve
            motor_angle = (degrees * axle_track * 2) / wheel_diameter
            motor_speed = max_speed * (speed / 100)
            
            if single_motor == TurnLeft:
                # Solo el motor izquierdo gira
                if degrees > 0:  # Giro a la derecha
                    left_motor.run_angle(motor_speed, motor_angle)
                else:  # Giro a la izquierda
                    left_motor.run_angle(-motor_speed, -motor_angle)
                right_motor.brake()  # Motor derecho estático
                
            elif single_motor == TurnRight:
                # Solo el motor derecho gira
                if degrees > 0:  # Giro a la derecha
                    right_motor.run_angle(-motor_speed, motor_angle)
                else:  # Giro a la izquierda
                    right_motor.run_angle(motor_speed, -motor_angle)
                left_motor.brake()  # Motor izquierdo estático
        else:
            # ... existing code ...
            # Fórmula corregida para calcular el ángulo del motor
            motor_angle = (degrees * axle_track) / wheel_diameter
            motor_speed = max_speed * (speed / 100)
            
            if degrees > 0:  # Giro a la derecha
                # Motor izquierdo hacia adelante, motor derecho hacia atrás
                left_motor.run_angle(motor_speed, motor_angle)
                right_motor.run_angle(-motor_speed, motor_angle)
            else:  # Giro a la izquierda
                # Motor derecho hacia adelante, motor izquierdo hacia atrás
                right_motor.run_angle(motor_speed, -motor_angle)
                left_motor.run_angle(-motor_speed, -motor_angle)
            
            # Frenar ambos motores
            left_motor.brake()
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
    def run_by_seconds(self, speed: float, seconds: float, angle: float = 0):
        drive_base = self.get_drive_base()
        left_motor = self.get_left_motor()
        right_motor = self.get_right_motor()
        drive_base.drive(self.get_max_speed() * (speed / 100), angle)
        wait(seconds * 1000)
        drive_base.stop()
        left_motor.brake()
        right_motor.brake()
    def reset_motors(self):
        left_motor = self.get_left_motor()
        right_motor = self.get_right_motor()
        left_motor.reset_angle(0)
        right_motor.reset_angle(0)
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

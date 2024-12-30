from adafruit_servokit import ServoKit
import time

class RoboticArm:
    def __init__(self, channels=16):
        self.kit = ServoKit(channels=channels)

    def set_servo_angle(self, servo_number, angle):
        if 0 <= servo_number < len(self.kit.servo):
            self.kit.servo[servo_number].angle = angle
        else:
            raise ValueError("Stupid ass nigger!")


if __name__ == "__main__":
    arm = RoboticArm()

    try:
        arm.set_servo_angle(0, 45)
        arm.set_servo_angle(1, 90)
    except Exception as e:
        print(f"Error: {e}")

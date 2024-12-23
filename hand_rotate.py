import pigpio
import time

pi = pigpio.pi()

SERVO_PIN = 20
pi.set_PWM_frequency(SERVO_PIN, 200)

def map(x: float, in_min: float, in_max: float, out_min: float, out_max: float) -> float:
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


def rotateHand():
    while True:
        setAngle(90)
        time.sleep(0.3)
        setAngle(-90)
        time.sleep(0.3)
def setAngle(angle: float):
    pulse_width = map(angle, -90, 90, 1000, 1900)
    pi.set_servo_pulsewidth(SERVO_PIN, pulse_width)

rotateHand()
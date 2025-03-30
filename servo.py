from adafruit_servokit import ServoKit
import time

kit = ServoKit(channels=16)

servos = [0, 1, 2, 3, 4, 5]
angles = list(range(0, 181, 5))

def move_servos():
    for angle in angles:
        for servo in servos:
            kit.servo[servo].angle = angle
        time.sleep(0.05)

while True:
    move_servos()
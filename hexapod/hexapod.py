from adafruit_servokit import ServoKit
import time

kit = ServoKit(channels=16)

delay = 0.02

for angle in range(0, 181, 1):
    for i in range(16):
        kit.servo[i].angle = angle
    time.sleep(delay)

for angle in range(180, -1, -1):
    for i in range(16):
        kit.servo[i].angle = angle
    time.sleep(delay)

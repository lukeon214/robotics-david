from adafruit_servokit import ServoKit
import time

kit = ServoKit(channels=16)

kit.servo[2].angle = 90
time.sleep(3)
kit.servo[2].angle = 0
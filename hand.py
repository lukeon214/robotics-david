from adafruit_servokit import ServoKit
import time

kit = ServoKit(channels=16)

kit.servo[2].angle = 0
kit.servo[2].angle = 180
kit.servo[2].angle = 90

kit.servo[1].angle = 0
from adafruit_servokit import ServoKit
import time
import threading

kit = ServoKit(channels=16)

kit.servo[1].angle = 0
time.sleep(2)
kit.servo[1].angle = 90
from adafruit_servokit import ServoKit
import time
import threading

kit = ServoKit(channels=16)

kit.servo[1].angle = 90
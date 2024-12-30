from adafruit_servokit import ServoKit
import time
kit = ServoKit(channels=16)

kit.continuous_servo[1].throttle = 1
time.sleep(3)
kit.continuous_servo[1].throttle = 0
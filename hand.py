from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

kit.servo[2].angle = 180
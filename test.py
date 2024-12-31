from adafruit_servokit import ServoKit
import time
import threading

kit = ServoKit(channels=16)

print("1. 0")
print("2. 90")
print("3. 180")

choice = input(int("$ "))

if choice == 1:
    kit.servo[1].angle = 0

if choice == 2:
    kit.servo[1].angle = 90

if choice == 3:
    kit.servo[1].angle = 180
from adafruit_servokit import ServoKit
import time

kit = ServoKit(channels=16)

servos = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
angles = [0, 30, 45, 60, 90, 120, 150, 180, 0]
 
def move_servos():
    for angle in angles:
        for servo in servos:
            kit.servo[servo].angle = angle
        time.sleep(0.2)

while True:
    move_servos()
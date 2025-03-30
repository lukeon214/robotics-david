from adafruit_servokit import ServoKit
import time

kit = ServoKit(channels=16)

servos = [0, 1, 2, 3, 4, 5]
angles = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 
 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180]

def move_servos():
    for angle in angles:
        for servo in servos:
            kit.servo[servo].angle = angle
        time.sleep(0.05)

while True:
    move_servos()
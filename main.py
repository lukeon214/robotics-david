from gpiozero import AngularServo
from time import sleep

servo = AngularServo(19, min_angle=-90, max_angle=180)

while True:
    servo.angle = 180
    sleep(3)

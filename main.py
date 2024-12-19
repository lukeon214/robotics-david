from gpiozero import AngularServo
from time import sleep

servo = AngularServo(19, min_angle=-90, max_angle=90)

while True:
    servo.angle = 90
    sleep(3)
    servo.angle = 90
    sleep(3)

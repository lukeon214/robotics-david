from gpiozero import AngularServo
from time import sleep

servo = AngularServo(19, min_angle=-90, max_angle=180)

while True:
    try:
        print("1. -90")
        print("2. -45")
        print("3. 0")
        print("4. 45")
        print("5. 90")

        nigg = int(input("Input: "))

        if nigg == 1:
            servo.angle = -90
        elif nigg == 2:
            servo.angle = -45
        elif nigg == 3:
            servo.angle = 0
        elif nigg == 4:
            servo.angle = 45
        elif nigg == 5:
            servo.angle = 90
    except ValueError:
        print("nigga")
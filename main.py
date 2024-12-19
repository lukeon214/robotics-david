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
        
        input = int(input("Input: "))

        if input == 1:
            servo.angle = -90
        elif input == 2:
            servo.angle = -45
        elif input == 3:
            servo.angle = 0
        elif input == 4:
            servo.angle = 45
        elif input == 5:
            servo.angle = 90
    except ValueError:
        print("nigga")
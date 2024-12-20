from gpiozero import AngularServo, LED
from sshkeyboard import listen_keyboard


servo1 = AngularServo(20, min_angle=-90, max_angle=90)

def listen1(key):
    if servo1.angle != 90:
        if key == "w":
            print("check 1. up")
            servo1.angle += 10
            print(servo1.angle)
    else:
        pass

    if servo1.angle != -90:
        if key == "s":
            print("check 1. down")
            servo1.angle -= 10
            print(servo1.angle)
    else:
        pass

listen_keyboard(listen1)
from gpiozero import AngularServo
from sshkeyboard import listen_keyboard


servo1 = AngularServo(19, min_angle=-90, max_angle=90)
servo2 = AngularServo(20, min_angle=-90, max_angle=90)
servo3 = AngularServo(21, min_angle=-90, max_angle=90)

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

def listen2(key):
    if servo2.angle != 90:
        if key == "e":
            print("check 2. up")
            servo2.angle += 10
            print(servo2.angle)
    else:
        pass

    if servo2.angle != -90:
        if key == "d":
            print("check 2. down")
            servo2.angle -= 10
            print(servo2.angle)

def listen3(key):
    if servo3.angle != 90:
        if key == "q":
            print("open")
            servo3.angle += 45
            print(servo3.angle)
    else:
        pass

    if servo3.angle != -90:
        if key == "a":
            print("close")
            servo3.angle -= 45
            print(servo3.angle)
    
listen_keyboard(listen1)
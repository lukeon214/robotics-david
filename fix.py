from gpiozero import AngularServo, LED, Motor
from sshkeyboard import listen_keyboard


servo1 = AngularServo(21, min_angle=-90, max_angle=90)

def listen(key):
    if servo1.angle != 90:
        if key == "w":
            print("up")
            servo1.angle += 10
            print(servo1.angle)
    else:
        pass

    if servo1.angle != -90:
        if key == "s":
            print("down")
            servo1.angle -= 10
            print(servo1.angle)
    
listen_keyboard(listen)

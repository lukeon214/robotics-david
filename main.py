from gpiozero import AngularServo, LED, Motor
from sshkeyboard import listen_keyboard

led = LED(31)
led.blink()

servo1 = AngularServo(19, min_angle=-90, max_angle=90)
servo2 = AngularServo(20, min_angle=-90, max_angle=90)
servo3 = AngularServo(21, min_angle=-90, max_angle=90)

def listen1(key):
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

def listen2(key):
    if servo2.angle != 90:
        if key == "w":
            print("up")
            servo2.angle += 10
            print(servo2.angle)
    else:
        pass

    if servo2.angle != -90:
        if key == "s":
            print("down")
            servo2.angle -= 10
            print(servo2.angle)

def listen3(key):
    if servo3.angle != 90:
        if key == "w":
            print("up")
            servo3.angle += 10
            print(servo3.angle)
    else:
        pass

    if servo3.angle != -90:
        if key == "s":
            print("down")
            servo3.angle -= 10
            print(servo3.angle)
    
listen_keyboard(listen1, listen2, listen3)
from gpiozero import AngularServo, LED
import keyboard
from sshkeyboard import listen_keyboard

led = LED(21)
led.blink()

servo1 = AngularServo(19, min_angle=-90, max_angle=90)
servo2 = AngularServo(20, min_angle=-90, max_angle=90)

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

def listen(key):
    if servo2.angle != 90:
        if key == "d":
            print("right")
            servo2.angle += 10
            print(servo2.angle)
    else:
        pass

    if servo2.angle != -90:
        if key == "a":
            print("left")
            servo2.angle -= 10
            print(servo2.angle)

    
listen_keyboard(listen)
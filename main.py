from gpiozero import AngularServo, LED, Motor
from sshkeyboard import listen_keyboard

led = LED(21)
led.blink()

servo1 = AngularServo(19, min_angle=-90, max_angle=90)
servo2 = Motor(20, forward=4, backward=14)

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

def listen2(key):
    if key == "d":
        print("right")
        servo2.forward()

    if key == "a":
        print("left")
        servo2.backward()

    
listen_keyboard(listen, listen2)
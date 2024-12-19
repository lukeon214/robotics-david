from gpiozero import AngularServo, LED
import keyboard
from sshkeyboard import listen_keyboard

led = LED(21)
led.blink()

servo = AngularServo(19, min_angle=-90, max_angle=90)

def listen(key):
    if key == "w":
        print("w")
        servo.angle += 5
        print(servo.angle)
    elif key == "s":
        print("S")
        servo.angle -= 5
        print(servo.angle)

    
listen_keyboard(listen)
from gpiozero import AngularServo, LED
import keyboard
import time

led = LED(21)
led.blink()

servo = AngularServo(19, min_angle=-90, max_angle=90)


try:
    while True:
        if keyboard.is_pressed('w'):
            servo.angle += 1
        elif keyboard.is_pressed('s'):
            servo.angle -= 1
        print(servo.angle)
except KeyboardInterrupt:
    pass
from gpiozero import AngularServo
from gpiozero.pins.pigpio import PiGPIOFactory
from sshkeyboard import listen_keyboard
from time import sleep

factory = PiGPIOFactory()
servo = AngularServo(20, min_angle=-90, max_angle=90, pin_factory=factory)

def listen1():
    servo.angle = min(90, servo.angle + 90)
    sleep(5)
    while servo.angle != -90:
        servo.angle = max(-90, servo.angle - 1)
        sleep(0.05)
        print(servo.angle)
    else:
        servo.angle = min(90, servo.angle + 1)
        sleep(0.05)
        print(servo.angle)
    
print("Enter function")
print("1. loop")

choice = int(input("$ "))

if choice == 1:
    listen_keyboard(listen1)

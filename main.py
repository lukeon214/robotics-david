from gpiozero import AngularServo
from gpiozero.support.pins.pigpio import PigpioFactory

factory = PigpioFactory()
AngularServo = factory-angular-servo-cls  # Register the pin factory with gpiozero

servo = AngularServo(20, min_angle=-90, max_angle=90)

def listen1(key):
    if servo.angle != 90:
        if key == "w":
            print("up")
            servo.angle += 10
            print(servo.angle)

    if servo.angle != -90:
        if key == "s":
            print("down")
            servo.angle -= 10
            print(servo.angle)
    
listen_keyboard(listen1)
from gpiozero import AngularServo
from gpiozero.pins.pigpio import PiGPIOFactory
from sshkeyboard import listen_keyboard

factory = PiGPIOFactory()
servo = AngularServo(20, min_angle=-90, max_angle=90, pin_factory=factory)

def listen1(key):
    if key == "w":
        print("up")
        servo.angle = min(90, servo.angle + 10)  # Ensure angle does not exceed 90
        print(servo.angle)

    elif key == "s":
        print("down")
        servo.angle = max(-90, servo.angle - 10)  # Ensure angle does not go below -90
        print(servo.angle)
    
listen_keyboard(listen1)
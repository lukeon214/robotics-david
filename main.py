from gpiozero import AngularServo, LED
import keyboard
import time

led = LED(21)
led.blink()

servo = AngularServo(19, min_angle=-90, max_angle=90)

servo_position = 0

try:
    while True:
        if keyboard.is_pressed('w'):
            if servo_position < 90:
                servo.angle = servo_position + 1
                servo_position += 1
        elif keyboard.is_pressed('s'):
            if servo_position > -90:
                servo.angle = servo_position - 1
                servo_position -= 1

        time.sleep(0.05)
except KeyboardInterrupt:
    pass
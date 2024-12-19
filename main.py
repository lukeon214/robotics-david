from gpiozero import AngularServo
from gpiozero import LED
from pynput import keyboard

led = LED(21)
led.blink()

servo = AngularServo(19, min_angle=-90, max_angle=90)

servo_position = 0

def on_press(key):
    global servo_position
    try:
        if key.char.lower() == 'w':
            if servo_position < 90:
                servo.angle = servo_position + 1
                servo_position += 1
        elif key.char.lower() == 's':
            if servo_position > -90:
                servo.angle = servo_position - 1
                servo_position -= 1

    except AttributeError:
        pass

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
from adafruit_servokit import ServoKit
import time
from sshkeyboard import listen_keyboard

kit = ServoKit(channels=16)

def on_key_press(key):
    if key == "a":
        kit.continuous_servo[0].throttle = 1.0

def on_key_release(key):
    if key == "a":
        kit.continuous_servo[0].throttle = 0.0

listen_keyboard(
    on_press=on_key_press,
    on_release=on_key_release
)
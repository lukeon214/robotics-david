from adafruit_servokit import ServoKit
import time
from sshkeyboard import listen_keyboard

kit = ServoKit(channels=16)

def listen(key):
    if key == "a":
        kit.continuous_servo[0].throttle = 1.0

    


listen_keyboard(listen)
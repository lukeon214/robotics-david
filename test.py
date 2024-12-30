from adafruit_servokit import ServoKit
import time
from sshkeyboard import listen_keyboard

kit = ServoKit(channels=16)

def listen(key):
    if key == "a":
        kit.continuous_servo[0].throttle = 0.5
        time.sleep(0.1)
        kit.continuous_servo[0].throttle = 0.0
    if key == "d":
        kit.continuous_servo[0].throttle = -0.5
        time.sleep(0.1)
        kit.continuous_servo[0].throttle = 0.0

listen_keyboard(listen)

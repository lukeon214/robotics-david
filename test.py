from adafruit_servokit import ServoKit
import time
from sshkeyboard import listen_keyboard

kit = ServoKit(channels=16)

def listen(key):
    kit.continuous_servo[0].throttle = 0.9
    time.sleep(5)
    kit.continuous_servo[0].throttle = 0.0


listen_keyboard(listen)
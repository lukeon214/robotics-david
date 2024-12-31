from adafruit_servokit import ServoKit
import time
from sshkeyboard import listen_keyboard

kit = ServoKit(channels=16)

kit.servo[2].angle = -90
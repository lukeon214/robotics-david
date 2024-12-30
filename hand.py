from adafruit_servokit import ServoKit
import time
from sshkeyboard import listen_keyboard

kit = ServoKit(channels=16)

kit.servo[3].angle = 90
time.sleep(3)
kit.servo[3].angle = 45
time.sleep(3)
kit.servo[3].angle = 0
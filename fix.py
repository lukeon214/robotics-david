from gpiozero import AngularServo, LED, Motor
from sshkeyboard import listen_keyboard


red = LED(21)
red.blink()
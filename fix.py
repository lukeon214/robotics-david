from gpiozero import AngularServo, LED, Motor
from sshkeyboard import listen_keyboard


red = LED(20)
red.blink()
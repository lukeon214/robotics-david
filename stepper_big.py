import RPi.GPIO as GPIO
import time

DIR = 18   # Direction pin
STEP = 17  # Step pin

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)

GPIO.output(DIR, GPIO.HIGH)  # Set direction

steps = 200  # One revolution (1.8° per step)

try:
    for _ in range(steps):
        GPIO.output(STEP, GPIO.HIGH)
        time.sleep(0.001)  # Step pulse width
        GPIO.output(STEP, GPIO.LOW)
        time.sleep(0.001)
finally:
    GPIO.cleanup()
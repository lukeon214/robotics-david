import RPi.GPIO as GPIO
import time

DIR = 18   # Direction pin
STEP = 17  # Step pin

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)

GPIO.output(DIR, GPIO.HIGH)  # Set direction

try:
    while True:
        GPIO.output(STEP, GPIO.HIGH)
        time.sleep(0.001)  # Step pulse width
        GPIO.output(STEP, GPIO.LOW)
        time.sleep(0.001)
except KeyboardInterrupt:
    print("Stopped by user.")
finally:
    GPIO.cleanup()
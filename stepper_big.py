import RPi.GPIO as GPIO
import time

DIR_PIN = 18   
STEP_PIN = 17  
STEPS_PER_REV = 200

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(DIR_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(STEP_PIN, GPIO.OUT, initial=GPIO.LOW)

def rotate_motor(revolutions=1, rpm=60, direction=True):
    steps = int(STEPS_PER_REV * revolutions)
    delay = 60.0 / (STEPS_PER_REV * rpm) / 2

    GPIO.output(DIR_PIN, GPIO.HIGH if direction else GPIO.LOW)
    
    for _ in range(steps):
        GPIO.output(STEP_PIN, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(STEP_PIN, GPIO.LOW)
        time.sleep(delay)

try:
    rotate_motor(revolutions=3, rpm=300, direction=True)

    rotate_motor(revolutions=3, rpm=300, direction=False)

finally:
    GPIO.output(STEP_PIN, GPIO.LOW)
    GPIO.output(DIR_PIN, GPIO.LOW)
    
    GPIO.cleanup()

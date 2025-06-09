import RPi.GPIO as GPIO
import time

DIR_PIN = 18   
STEP_PIN = 17  

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(DIR_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(STEP_PIN, GPIO.OUT, initial=GPIO.LOW)

def motor(direction=True):
    while True:
        GPIO.output(DIR_PIN, GPIO.HIGH if direction else GPIO.LOW)
        GPIO.output(STEP_PIN, GPIO.HIGH)
        time.sleep(0.001)
        GPIO.output(STEP_PIN, GPIO.LOW)
        time.sleep(0.001)
    
try:
    motor(direction=True)

finally:
    GPIO.output(STEP_PIN, GPIO.LOW)
    GPIO.output(DIR_PIN, GPIO.LOW)
    
    GPIO.cleanup()
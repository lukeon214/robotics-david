import RPi.GPIO as GPIO

DIR_PIN = 18   
STEP_PIN = 17  

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(DIR_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(STEP_PIN, GPIO.OUT, initial=GPIO.LOW)

while True:
    GPIO.output(STEP_PIN, GPIO.HIGH)
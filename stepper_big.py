import RPi.GPIO as GPIO
import time

DIR = 18   # Direction pin
STEP = 17  # Step pin

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)

GPIO.output(DIR, GPIO.HIGH)  # Set direction (HIGH = CW, LOW = CCW)

angle_per_step = 1.8  # degrees
current_angle = 0.0

try:
    while True:
        GPIO.output(STEP, GPIO.HIGH)
        time.sleep(0.001)  # High pulse
        GPIO.output(STEP, GPIO.LOW)
        time.sleep(0.001)  # Low pulse

        current_angle += angle_per_step
        if current_angle >= 360:
            current_angle -= 360

        print(f"Current Angle: {current_angle:.1f}°")
except KeyboardInterrupt:
    print("Stopped by user.")
finally:
    GPIO.cleanup()
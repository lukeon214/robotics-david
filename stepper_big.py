import RPi.GPIO as GPIO
import time

# GPIO pin setup
DIR = 18     # Direction GPIO pin
STEP = 17    # Step GPIO pin
CW = GPIO.HIGH   # Clockwise
CCW = GPIO.LOW   # Counter-clockwise

# Motor setup
SPR = 200         # Steps per revolution (1.8°/step)

# Initialize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)

# Set direction
GPIO.output(DIR, CW)  # Change to CCW for reverse

step_delay = 0.01     # 10ms delay = 100 steps/sec (slow and safe)

print("Rotating motor 1 revolution clockwise...")
try:
    for step in range(SPR):  # One full revolution
        GPIO.output(STEP, GPIO.HIGH)
        time.sleep(step_delay)
        GPIO.output(STEP, GPIO.LOW)
        time.sleep(step_delay)

    time.sleep(1)  # Short pause

    print("Now rotating 1 revolution counter-clockwise...")
    GPIO.output(DIR, CCW)
    time.sleep(0.5)

    for step in range(SPR):
        GPIO.output(STEP, GPIO.HIGH)
        time.sleep(step_delay)
        GPIO.output(STEP, GPIO.LOW)
        time.sleep(step_delay)

    print("Test complete.")

except KeyboardInterrupt:
    print("\nInterrupted by user.")

finally:
    GPIO.cleanup()

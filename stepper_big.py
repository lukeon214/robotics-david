import RPi.GPIO as GPIO
import time

# === Motor Driver GPIO Pins ===
DIR_PIN = 18   # Direction GPIO pin
STEP_PIN = 17  # Step GPIO pin

# === Motor Constants ===
STEPS_PER_REV = 200   # Adjust for microstepping if needed

# === Setup ===
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(DIR_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(STEP_PIN, GPIO.OUT, initial=GPIO.LOW)

def rotate_motor(revolutions=1, rpm=60, direction=True):
    """
    Rotate the stepper motor.
    
    Parameters:
        revolutions (float): Number of revolutions
        rpm (float): Speed in revolutions per minute
        direction (bool): True for one way, False for opposite
    """
    steps = int(STEPS_PER_REV * revolutions)
    delay = 60.0 / (STEPS_PER_REV * rpm) / 2  # time between step transitions

    GPIO.output(DIR_PIN, GPIO.HIGH if direction else GPIO.LOW)
    
    for _ in range(steps):
        GPIO.output(STEP_PIN, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(STEP_PIN, GPIO.LOW)
        time.sleep(delay)

try:
    # Example usage: rotate 3 full turns at 90 RPM clockwise
    rotate_motor(revolutions=3, rpm=1000, direction=True)

    # Then rotate back 1 turn at 30 RPM counter-clockwise
    rotate_motor(revolutions=3, rpm=1000, direction=False)

finally:
    # Explicitly set pins LOW before cleanup
    GPIO.output(STEP_PIN, GPIO.LOW)
    GPIO.output(DIR_PIN, GPIO.LOW)
    
    GPIO.cleanup()

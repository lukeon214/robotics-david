import RPi.GPIO as GPIO
import time

DIR  = 18     # GPIO pin numbers
STEP = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR,  GPIO.OUT, initial=GPIO.HIGH)   # CW
GPIO.setup(STEP, GPIO.OUT, initial=GPIO.LOW)

ANGLE_PER_STEP = 1.8          # full-step, no micro-stepping
current_angle  = 0.0

try:
    while True:
        GPIO.output(STEP, GPIO.HIGH)
        time.sleep(0.001)      # 1 ms high
        GPIO.output(STEP, GPIO.LOW)
        time.sleep(0.001)      # 1 ms low  → 500 steps/s ≈ 1 rev/s

        current_angle += ANGLE_PER_STEP
        if current_angle >= 360:
            current_angle -= 360

        print(f"{current_angle:6.1f}°", end="\r", flush=True)

except KeyboardInterrupt:
    print("\nStopped at {:.1f}°".format(current_angle))
finally:
    GPIO.cleanup()

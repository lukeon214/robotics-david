import RPi.GPIO as GPIO
import time

# GPIO pin setup
IN1 = 17
IN2 = 18
IN3 = 27
IN4 = 22
pins = [IN1, IN2, IN3, IN4]

# Step sequence for 28BYJ-48
seq = [
    [1,0,0,1],
    [1,0,0,0],
    [1,1,0,0],
    [0,1,0,0],
    [0,1,1,0],
    [0,0,1,0],
    [0,0,1,1],
    [0,0,0,1]
]

STEP_ANGLE = 360.0 / 2048  # ≈ 0.17578°

GPIO.setmode(GPIO.BCM)

for pin in pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)

# Step counter
step_count = 0

try:
    while True:
        for step in seq:
            for pin in range(4):
                GPIO.output(pins[pin], step[pin])
            step_count += 1
            angle = step_count * STEP_ANGLE
            print(f"Current angle: {angle:.2f}°")
            time.sleep(0.002)  # Adjust speed
except KeyboardInterrupt:
    print("Stopped at angle: {:.2f}°".format(step_count * STEP_ANGLE))
    GPIO.cleanup()

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

GPIO.setmode(GPIO.BCM)

for pin in pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)

try:
    while True:
        for step in seq:
            for pin in range(4):
                GPIO.output(pins[pin], step[pin])
            time.sleep(0.002)  # Adjust speed
except KeyboardInterrupt:
    print("Stopped")
    GPIO.cleanup()
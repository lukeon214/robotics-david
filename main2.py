import pigpio
import time
import threading

pi = pigpio.pi()

# Set up LED pin
LED_PIN = 26
pi.set_mode(LED_PIN, pigpio.OUTPUT)

# Set up servo pin
SERVO_PIN = 20
pi.set_PWM_frequency(SERVO_PIN, 200)

# Map function to scale values
def map(x: float, in_min: float, in_max: float, out_min: float, out_max: float) -> float:
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

# Function to control the servo angle
def setAngleLoop():
    while True:
        for i in range(-90, 90):
            setAngle(float(i))
            time.sleep(0.01)
            print(f"Angle: {float(i)}")

        for i in range(-90, 90)[::-1]:
            setAngle(float(i))
            time.sleep(0.01)
            print(f"Angle: {float(i)}")

# Helper function to set servo angle
def setAngle(angle: float):
    pulse_width = map(angle, -90, 90, 1000, 1900)
    pi.set_servo_pulsewidth(SERVO_PIN, pulse_width)

# Function to blink the LED
def blink_led():
    while True:
        pi.write(LED_PIN, 1)  # Turn LED on
        time.sleep(0.5)
        pi.write(LED_PIN, 0)  # Turn LED off
        time.sleep(0.5)

# Create threads for the LED and servo functions
led_thread = threading.Thread(target=blink_led)
servo_thread = threading.Thread(target=setAngleLoop)

# Start the threads
led_thread.start()
servo_thread.start()

# Wait for threads to complete (this script will run indefinitely)
led_thread.join()
servo_thread.join()

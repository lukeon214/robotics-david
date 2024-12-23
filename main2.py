import pigpio
import time
import threading

pi = pigpio.pi()

LED_PIN = 26
pi.set_mode(LED_PIN, pigpio.OUTPUT)

SERVO_PIN = 20
pi.set_PWM_frequency(SERVO_PIN, 200)

def map(x: float, in_min: float, in_max: float, out_min: float, out_max: float) -> float:
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


def setAngleLoop():
    while True:
        for i in range(-90, 90):
            setAngle(float(i))
            time.sleep(0.05)
            print(f"Angle: {float(i)}")

        for i in range(-90, 90)[::-1]:
            setAngle(float(i))
            time.sleep(0.05)
            print(f"Angle: {float(i)}")

def setAngle(angle: float):
    pulse_width = map(angle, -90, 90, 1000, 1900)
    pi.set_servo_pulsewidth(SERVO_PIN, pulse_width)

# Function to blink the LED
def blink_led():
    while True:
        pi.write(LED_PIN, 1) 
        time.sleep(0.5)
        pi.write(LED_PIN, 0)  
        time.sleep(0.5)

led_thread = threading.Thread(target=blink_led)
servo_thread = threading.Thread(target=setAngleLoop)

led_thread.start()
servo_thread.start()

led_thread.join()
servo_thread.join()

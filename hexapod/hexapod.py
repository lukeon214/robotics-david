from adafruit_servokit import ServoKit
import time

kit = ServoKit(channels=16)

startup_angles = {
    0: 140,
    1: 90
}

def startup_servos():
    print("Starting up servos...")
    for pin, angle in startup_angles.items():
        print(f"Setting servo on pin {pin} to angle {angle}")
        kit.servo[pin].angle = angle
        time.sleep(0.2)

    print("Servos initialized.")

if __name__ == "__main__":
    startup_servos()
from time import sleep
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

DEGREES_PER_SECOND = 360

def control_servo(pin, angle):
    if pin == 1:
        rotate_continuous_servo(pin, angle)
    else:
        set_normal_servo(pin, angle)

def set_normal_servo(pin, angle):
    if not (0 <= angle <= 180):
        print(f"Error: Angle {angle} is out of range (0-180).")
        return
    
    try:
        kit.servo[pin].angle = angle
        print(f"Normal servo on pin {pin} set to {angle} degrees.")
    except Exception as e:
        print(f"Error: {e}")

def rotate_continuous_servo(pin, angle, speed=1.0):
    if not (0 < speed <= 1.0):
        print("Error: Speed must be between 0 and 1.")
        return

    rotation_time = abs(angle) / (DEGREES_PER_SECOND * speed)
    direction = 1 if angle > 0 else -1

    try:
        kit.continuous_servo[pin].throttle = direction * speed
        print(f"Rotating continuous servo on pin {pin} for {rotation_time:.2f} seconds.")
        sleep(rotation_time)

        kit.continuous_servo[pin].throttle = 0
        print(f"Continuous servo on pin {pin} stopped.")
    except Exception as e:
        print(f"Error: {e}")

def main():
    print("Servo Controller")
    print("Type commands in the format: <pin> <angle>")
    print("Type 'exit' to quit.")

    while True:
        command = input("Enter command: ")
        if command.lower() == "exit":
            break
        
        try:
            pin, angle = map(int, command.split())
            control_servo(pin, angle)
        except ValueError:
            print("Error!")

if __name__ == "__main__":
    main()

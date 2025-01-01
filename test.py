from time import sleep
from adafruit_servokit import ServoKit

# Initialize ServoKit
kit = ServoKit(channels=16)

# Known speed of the continuous servo in degrees per second (at full throttle)
DEGREES_PER_SECOND = 285  # Adjust this based on your servo's specifications

def rotate_continuous_servo(pin, angle, speed=1.0):
    """
    Rotate a continuous servo to simulate a normal servo angle rotation.
    :param pin: The pin where the servo is connected.
    :param angle: The desired rotation in degrees.
    :param speed: Throttle value (0 to 1). Default is full speed.
    """
    if not (0 < speed <= 1.0):
        print("Error: Speed must be between 0 and 1.")
        return

    # Calculate rotation time
    rotation_time = abs(angle) / (DEGREES_PER_SECOND * speed)
    direction = 1 if angle > 0 else -1  # Determine direction based on angle

    try:
        # Start rotation
        kit.continuous_servo[pin].throttle = direction * speed
        print(f"Rotating servo on pin {pin} for {rotation_time:.2f} seconds.")
        sleep(rotation_time)

        # Stop rotation
        kit.continuous_servo[pin].throttle = 0
        print(f"Servo on pin {pin} stopped.")
    except Exception as e:
        print(f"Error: {e}")

def main():
    print("Continuous Servo Controller")
    print("Type commands in the format: <pin> <angle>")
    print("Type 'exit' to quit.")

    while True:
        command = input("Enter command: ")
        if command.lower() == "exit":
            print("Exiting...")
            break
        
        try:
            pin, angle = map(int, command.split())
            rotate_continuous_servo(pin, angle)
        except ValueError:
            print("Invalid input. Please enter the command in the format: <pin> <angle>.")

if __name__ == "__main__":
    main()

from time import sleep
from adafruit_servokit import ServoKit

# Initialize ServoKit
kit = ServoKit(channels=16)

# Known speed of the continuous servo in degrees per second (at full throttle)
DEGREES_PER_SECOND = 280  # Adjust based on your servo's specifications

def control_servo(pin, angle):
    """
    Control both normal and continuous servos.
    - For continuous servo (e.g., pin 1), simulate angle control.
    - For normal servos, directly set the angle.
    :param pin: The pin where the servo is connected.
    :param angle: The desired angle or rotation.
    """
    if pin == 1:
        # Handle continuous servo
        rotate_continuous_servo(pin, angle)
    else:
        # Handle normal servo
        set_normal_servo(pin, angle)

def set_normal_servo(pin, angle):
    """
    Set the angle of a normal servo.
    :param pin: The pin number where the servo is connected.
    :param angle: The angle to set the servo to (0-180 degrees).
    """
    if not (0 <= angle <= 180):
        print(f"Error: Angle {angle} is out of range (0-180).")
        return
    
    try:
        kit.servo[pin].angle = angle
        print(f"Normal servo on pin {pin} set to {angle} degrees.")
    except Exception as e:
        print(f"Error: {e}")

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
        print(f"Rotating continuous servo on pin {pin} for {rotation_time:.2f} seconds.")
        sleep(rotation_time)

        # Stop rotation
        kit.continuous_servo[pin].throttle = 0
        print(f"Continuous servo on pin {pin} stopped.")
    except Exception as e:
        print(f"Error: {e}")

def main():
    print("Combined Servo Controller")
    print("Type commands in the format: <pin> <angle>")
    print("Type 'exit' to quit.")

    while True:
        command = input("Enter command: ")
        if command.lower() == "exit":
            print("Exiting...")
            break
        
        try:
            pin, angle = map(int, command.split())
            control_servo(pin, angle)
        except ValueError:
            print("Invalid input. Please enter the command in the format: <pin> <angle>.")

if __name__ == "__main__":
    main()

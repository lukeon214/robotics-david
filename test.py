from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

def set_servo_angle(pin, angle):
    try:
        kit.servo[pin].angle = angle
        print(f"Servo on pin {pin} set to {angle} degrees.")
    except Exception as e:
        print(f"Unexpected error: {e}")

def main():
    print("Robotic Arm Controller")
    print("Type commands in the format: <pin> <angle>")
    print("Type 'exit' to quit.")

    while True:
        command = input("Enter command: ")
        if command.lower() == "exit":
            break

if __name__ == "__main__":
    main()

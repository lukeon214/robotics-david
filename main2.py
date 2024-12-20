import pigpio
import keyboard  # Library to detect key presses

pi = pigpio.pi()

# Map function to scale values
def map(x: float, in_min: float, in_max: float, out_min: float, out_max: float) -> float:
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

# Set servo angle
def set_angle(angle: float):
    pi.set_servo_pulsewidth(20, map(angle, -90, 90, 1000, 1900))

# Main loop
def main():
    angle = 0  # Start angle
    step = 1   # Angle increment step
    print("Press 'w' to increase angle, 's' to decrease angle, and 'q' to quit.")

    try:
        while True:
            if keyboard.is_pressed("w"):  # Increase angle
                angle = min(angle + step, 90)  # Clamp to max angle of 90
                set_angle(angle)
                print(f"Angle increased to: {angle}")
            elif keyboard.is_pressed("s"):  # Decrease angle
                angle = max(angle - step, -90)  # Clamp to min angle of -90
                set_angle(angle)
                print(f"Angle decreased to: {angle}")
            elif keyboard.is_pressed("q"):  # Quit the program
                print("Exiting program.")
                break
    finally:
        pi.stop()  # Ensure pigpio is stopped

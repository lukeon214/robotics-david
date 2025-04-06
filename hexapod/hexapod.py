import math
import time
from adafruit_servokit import ServoKit

# Initialize the 16-channel PWM driver
kit = ServoKit(channels=16)

# Leg segment lengths in mm
L1 = 110.0  # Upper leg (hip to knee)
L2 = 150.0  # Lower leg (knee to foot)

def inverse_kinematics(x, y):
    r = math.sqrt(x * x + y * y)

    if r > (L1 + L2):
        print("Target out of reach! Clamping to maximum reachable distance.")
        r = L1 + L2

    phi = math.degrees(math.atan2(y, x))
    
    cos_delta = (L1**2 + r**2 - L2**2) / (2 * L1 * r)
    cos_delta = max(min(cos_delta, 1), -1)
    delta = math.degrees(math.acos(cos_delta))
    
    theta1_mech = phi - delta
    servo_hip = theta1_mech + 90

    cos_gamma = (L1**2 + L2**2 - r**2) / (2 * L1 * L2)
    cos_gamma = max(min(cos_gamma, 1), -1)
    gamma = math.degrees(math.acos(cos_gamma))
    servo_knee = 180 - gamma

    servo_hip = max(0, min(180, servo_hip))
    servo_knee = max(0, min(180, servo_knee))

    return servo_hip, servo_knee

def move_leg_to(x, y):
    hip_angle, knee_angle = inverse_kinematics(x, y)
    print(f"Moving to ({x:.1f}, {y:.1f}) -> Hip: {hip_angle:.1f}°, Knee: {knee_angle:.1f}°")

    kit.servo[0].angle = hip_angle
    kit.servo[1].angle = knee_angle
    time.sleep(0.5)

def interactive_control():
    print("Leg IK control started.")
    print("Type coordinates as: x y")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("Enter target x y: ").strip()
        
        if user_input.lower() in ['exit', 'quit']:
            print("Exiting...")
            break

        try:
            x_str, y_str = user_input.split()
            x = float(x_str)
            y = float(y_str)
            move_leg_to(x, y)
        except ValueError:
            print("Invalid input! Please enter two numbers separated by space (e.g., 100 50).")

if __name__ == "__main__":
    interactive_control()
import math
import time
from adafruit_servokit import ServoKit

# Initialize the 16-channel PWM driver
kit = ServoKit(channels=16)

# Leg segment lengths in mm
L1 = 110.0  # Upper leg (hip to knee)
L2 = 150.0  # Lower leg (knee to foot)

def inverse_kinematics(x, y):
    """
    Given a target foot position (x, y) in mm relative to the hip joint,
    calculate the required servo angles for the hip and knee.
    
    Coordinate system:
      - x axis: horizontal (forward)
      - y axis: vertical downward

    Servo mapping:
      - Hip servo (servo 0): 0° means leg down, 90° means horizontal.
      - Knee servo (servo 1): computed as 180 - (internal knee angle)
        so that when the leg is nearly extended (internal angle ~40°), the servo is at ~140°.
    """
    # Distance from hip to target point
    r = math.sqrt(x * x + y * y)
    
    # Clamp r if out of reach
    if r > (L1 + L2):
        print("Target out of reach! Clamping to maximum reachable distance.")
        r = L1 + L2

    # Angle from horizontal to target (in degrees)
    phi = math.degrees(math.atan2(y, x))
    
    # Calculate angle for the upper leg using law of cosines
    cos_delta = (L1**2 + r**2 - L2**2) / (2 * L1 * r)
    cos_delta = max(min(cos_delta, 1), -1)
    delta = math.degrees(math.acos(cos_delta))
    
    # Mechanical hip angle relative to horizontal
    theta1_mech = phi - delta
    # Map to servo angle: add 90° because servo 0 = 0° means down and 90° means horizontal
    servo_hip = theta1_mech + 90

    # Calculate knee angle using law of cosines
    cos_gamma = (L1**2 + L2**2 - r**2) / (2 * L1 * L2)
    cos_gamma = max(min(cos_gamma, 1), -1)
    gamma = math.degrees(math.acos(cos_gamma))
    # Map to servo angle (so that when gamma is around 40°, servo reads ~140°)
    servo_knee = 180 - gamma

    # Clamp angles between 0 and 180
    servo_hip = max(0, min(180, servo_hip))
    servo_knee = max(0, min(180, servo_knee))

    return servo_hip, servo_knee

def move_leg_to(x, y):
    """Moves the leg to the target (x, y) position by calculating and setting servo angles."""
    hip_angle, knee_angle = inverse_kinematics(x, y)
    print(f"Moving to (x={x:.1f}, y={y:.1f}) -> Hip: {hip_angle:.1f}°, Knee: {knee_angle:.1f}°")
    
    kit.servo[0].angle = hip_angle
    kit.servo[1].angle = knee_angle
    time.sleep(0.5)  # Allow time for servos to reach position

def square_trajectory():
    """
    Moves the leg through a square-like path:
      1. Max Up (lifted leg)
      2. Max Forward (foot extended forward)
      3. Max Back (foot pulled back)
      4. Return to Max Up
    """
    # Define the positions for the trajectory:
    positions = [
        (225, 20),    # Max Up: leg lifted
        (300, 150),   # Max Forward: foot extended forward
        (150, 150),   # Max Back: foot pulled back
        (225, 20)     # Return to Max Up
    ]
    
    print("Starting square trajectory...")
    for (x, y) in positions:
        move_leg_to(x, y)
        time.sleep(1)  # Pause between moves for clarity
    print("Completed square trajectory.")

if __name__ == "__main__":
    # Run the square trajectory routine
    square_trajectory()

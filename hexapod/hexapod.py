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
      - Knee servo (servo 1): computed as 180 - (angle between links)
        so that when the leg is nearly extended (with a 40° bend), the servo is at 140°.
    """
    # Distance from hip to foot target
    r = math.sqrt(x * x + y * y)
    
    # Check for reachability – if r > L1 + L2, clamp to maximum reachable distance.
    if r > (L1 + L2):
        print("Target out of reach! Clamping to maximum reachable distance.")
        r = L1 + L2

    # Angle (in degrees) from horizontal (x-axis) to the target point.
    # (Note: arctan2 returns an angle in radians; convert to degrees.)
    phi = math.degrees(math.atan2(y, x))
    
    # Calculate the angle between the first link and the line from hip to foot using the law of cosines.
    cos_delta = (L1**2 + r**2 - L2**2) / (2 * L1 * r)
    # Clamp cos_delta to avoid math domain errors.
    cos_delta = max(min(cos_delta, 1), -1)
    delta = math.degrees(math.acos(cos_delta))
    
    # Mechanical angle for the hip joint relative to horizontal.
    # (Subtract delta so that when the target is in the neutral configuration, we get 0°.)
    theta1_mech = phi - delta
    # Map to servo angle: since for the hip servo 0° is down and 90° is horizontal,
    # add 90° (i.e. servo_hip = 90 + theta1_mech).
    servo_hip = theta1_mech + 90

    # Compute the internal knee joint angle using the law of cosines.
    cos_gamma = (L1**2 + L2**2 - r**2) / (2 * L1 * L2)
    cos_gamma = max(min(cos_gamma, 1), -1)
    gamma = math.degrees(math.acos(cos_gamma))
    # For the knee, we use:
    #   servo_knee = 180 - gamma
    # so that when the leg is nearly extended (gamma near 40°), servo_knee ~ 140°.
    servo_knee = 180 - gamma

    # Clamp the computed servo angles within 0° to 180°.
    servo_hip = max(0, min(180, servo_hip))
    servo_knee = max(0, min(180, servo_knee))

    return servo_hip, servo_knee

def move_leg_to(x, y):
    """Moves the leg to the target (x, y) position by calculating and setting servo angles."""
    hip_angle, knee_angle = inverse_kinematics(x, y)
    print(f"Moving leg to x={x:.1f} mm, y={y:.1f} mm -> Hip: {hip_angle:.1f}°, Knee: {knee_angle:.1f}°")
    
    kit.servo[0].angle = hip_angle
    kit.servo[1].angle = knee_angle
    time.sleep(0.5)  # Delay to allow the servos to move

if __name__ == "__main__":
    # Compute a "neutral" target position corresponding to our startup configuration.
    # For a horizontal hip (servo 0 at 90°) and a knee at 140°,
    # using our IK equations, this roughly corresponds to:
    #   x = L1 + L2*cos(40°)  and  y = L2*sin(40°)
    neutral_x = L1 + L2 * math.cos(math.radians(40))
    neutral_y = L2 * math.sin(math.radians(40))
    
    print("Initializing leg to neutral configuration...")
    move_leg_to(neutral_x, neutral_y)
    print("Leg in neutral position.")
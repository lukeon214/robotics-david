from adafruit_servokit import ServoKit
import time
import math

# Initialize servos
kit = ServoKit(channels=16)

# Leg segment lengths (adjust based on your robot's measurements)
L1 = 5.0  # Length from servo 0 to servo 1 (cm)
L2 = 5.0  # Length from servo 1 to foot (cm)

# Servo offsets/constraints (adjust based on your setup)
SERVO0_OFFSET = 140  # Default angle for servo 0 (body joint)
SERVO1_OFFSET = 90   # Default angle for servo 1 (knee)
SERVO_LIMITS = [(0, 180), (0, 180)]  # Min/max angles for each servo

def setup_servos():
    # Initialize to default angles
    kit.servo[0].angle = SERVO0_OFFSET
    kit.servo[1].angle = SERVO1_OFFSET
    time.sleep(1)

def calculate_ik(x, y):
    distance = math.sqrt(x**2 + y**2)
    if distance > (L1 + L2) or distance < abs(L1 - L2):
        print("Error: Target out of reach!")
        return None, None
    
    theta2 = math.acos((x**2 + y**2 - L1**2 - L2**2) / (2 * L1 * L2))
    theta1 = math.atan2(y, x) - math.atan2((L2 * math.sin(theta2)), (L1 + L2 * math.cos(theta2)))
    
    theta1_deg = math.degrees(theta1) + SERVO0_OFFSET
    theta2_deg = math.degrees(theta2) + SERVO1_OFFSET
    
    # Clamp angles to servo limits
    theta1_deg = max(min(theta1_deg, SERVO_LIMITS[0][1]), SERVO_LIMITS[0][0])
    theta2_deg = max(min(theta2_deg, SERVO_LIMITS[1][1]), SERVO_LIMITS[1][0])
    
    return theta1_deg, theta2_deg

def move_leg(x, y, duration=1.0):
    theta1, theta2 = calculate_ik(x, y)
    if theta1 is None:
        return
    
    # Smoothly move servos
    steps = 20
    current_theta1 = kit.servo[0].angle
    current_theta2 = kit.servo[1].angle
    delta1 = (theta1 - current_theta1) / steps
    delta2 = (theta2 - current_theta2) / steps
    
    for _ in range(steps):
        current_theta1 += delta1
        current_theta2 += delta2
        kit.servo[0].angle = current_theta1
        kit.servo[1].angle = current_theta2
        time.sleep(duration / steps)

# Example usage
if __name__ == "__main__":
    setup_servos()
    time.sleep(1)
    
    # Move foot in a square pattern
    targets = [
        (7, 7),   # Forward-right
        (7, -7),  # Backward-right
        (-7, -7), # Backward-left
        (-7, 7),  # Forward-left
    ]
    
    for x, y in targets:
        print(f"Moving to ({x}, {y})")
        move_leg(x, y)
        time.sleep(0.5)
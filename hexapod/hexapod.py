from adafruit_servokit import ServoKit
import time
import math

# Initialize servos
kit = ServoKit(channels=16)

# Leg segment lengths (in mm)
L1 = 110  # Length from body joint (servo 0) to knee (servo 1)
L2 = 150  # Length from knee to foot

# Servo configuration
SERVO0_NEUTRAL = 90   # Body joint default (0° = down, 180° = up)
SERVO1_NEUTRAL = 140  # Knee joint default (0° = up, 180° = down)
SERVO_LIMITS = [(0, 180), (0, 180)]  # Both servos can move 0-180°

def setup_servos():
    """Initialize servos to their default positions"""
    kit.servo[0].angle = SERVO0_NEUTRAL
    kit.servo[1].angle = SERVO1_NEUTRAL
    time.sleep(1)
    print("Servos initialized to neutral positions")

def calculate_ik(x, y):
    """Convert X,Y coordinates to servo angles with proper direction mapping"""
    # Convert to centimeters for calculation
    x_cm = x / 10
    y_cm = y / 10
    L1_cm = L1 / 10
    L2_cm = L2 / 10
    
    distance = math.hypot(x_cm, y_cm)
    
    # Check reachability
    if distance > (L1_cm + L2_cm) or distance < abs(L1_cm - L2_cm):
        print(f"Target ({x},{y}) unreachable")
        return None, None

    # Calculate angles using inverse kinematics
    theta2 = math.acos((x_cm**2 + y_cm**2 - L1_cm**2 - L2_cm**2) / (2 * L1_cm * L2_cm))
    theta1 = math.atan2(y_cm, x_cm) - math.atan2(L2_cm * math.sin(theta2), L1_cm + L2_cm * math.cos(theta2))

    # Convert to degrees and adjust for servo direction
    theta1_deg = math.degrees(theta1)
    theta2_deg = math.degrees(theta2)
    
    # Convert to servo angles (0° directions as specified)
    servo0_angle = 90 - theta1_deg  # Invert body joint direction
    servo1_angle = 180 - theta2_deg  # Invert knee joint direction
    
    # Apply limits
    servo0_angle = max(SERVO_LIMITS[0][0], min(SERVO_LIMITS[0][1], servo0_angle))
    servo1_angle = max(SERVO_LIMITS[1][0], min(SERVO_LIMITS[1][1], servo1_angle))

    return round(servo0_angle, 1), round(servo1_angle, 1)

def move_leg(servo0_angle, servo1_angle, duration=1.0):
    """Smoothly move servos to target angles"""
    current0 = kit.servo[0].angle
    current1 = kit.servo[1].angle
    steps = 20
    
    for step in range(steps):
        interp0 = current0 + (servo0_angle - current0) * (step + 1) / steps
        interp1 = current1 + (servo1_angle - current1) * (step + 1) / steps
        
        kit.servo[0].angle = interp0
        kit.servo[1].angle = interp1
        time.sleep(duration / steps)

# Example usage: Draw a rectangle pattern
if __name__ == "__main__":
    setup_servos()
    time.sleep(1)
    
    # Target positions in mm (relative to body joint)
    targets = [
        (200, 0),   # Forward
        (200, 100),  # Forward-down
        (100, 100),  # Backward-down
        (100, 0),    # Backward
    ]
    
    for x, y in targets:
        print(f"\nMoving to ({x}mm, {y}mm)")
        angles = calculate_ik(x, y)
        if angles:
            print(f"Servo angles: {angles}")
            move_leg(angles[0], angles[1])
            time.sleep(0.3)
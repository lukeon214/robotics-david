from adafruit_servokit import ServoKit
import time
import math

# Initialize servos
kit = ServoKit(channels=16)

# Leg configuration (in millimeters)
L1 = 110  # Body joint to knee
L2 = 150  # Knee to foot
SERVO0_NEUTRAL = 90   # Body joint (0°=down, 180°=up)
SERVO1_NEUTRAL = 140  # Knee joint (0°=up, 180°=down)

def setup_servos():
    """Reset servos to neutral position"""
    kit.servo[0].angle = SERVO0_NEUTRAL
    kit.servo[1].angle = SERVO1_NEUTRAL
    time.sleep(1)
    print("Servos reset to neutral position")

def calculate_ik(x, y):
    """Convert X/Y coordinates to servo angles with proper direction handling"""
    # Convert to centimeters for calculation
    x_cm = x / 10
    y_cm = y / 10
    L1_cm = L1 / 10
    L2_cm = L2 / 10
    
    distance = math.sqrt(x**2 + y**2) / 10  # Distance in cm
    
    # Check if target is reachable
    if distance > (L1_cm + L2_cm) or distance < abs(L1_cm - L2_cm):
        return None, None

    # IK Calculations
    theta2 = math.acos((x_cm**2 + y_cm**2 - L1_cm**2 - L2_cm**2) / (2 * L1_cm * L2_cm))
    theta1 = math.atan2(y_cm, x_cm) - math.atan2(L2_cm * math.sin(theta2), L1_cm + L2_cm * math.cos(theta2))
    
    # Convert to degrees and adjust for servo directions
    servo0_angle = 90 + math.degrees(theta1)  # 0°=down, 180°=up
    servo1_angle = math.degrees(theta2)       # 0°=up, 180°=down
    
    # Apply servo limits
    servo0_angle = max(0, min(180, servo0_angle))
    servo1_angle = max(0, min(180, servo1_angle))
    
    return round(servo0_angle, 1), round(servo1_angle, 1)

def move_leg(servo0_angle, servo1_angle, duration=0.5):
    """Smooth movement to target angles"""
    current0 = kit.servo[0].angle
    current1 = kit.servo[1].angle
    steps = 20
    
    for step in range(steps):
        interp0 = current0 + (servo0_angle - current0) * (step + 1) / steps
        interp1 = current1 + (servo1_angle - current1) * (step + 1) / steps
        kit.servo[0].angle = interp0
        kit.servo[1].angle = interp1
        time.sleep(duration / steps)

def wave_movement():
    """Automatic wave pattern moving above and below neutral"""
    # X positions (front to back)
    x_values = list(range(200, 100, -5)) + list(range(100, 200, 5))
    
    # Y values (sine wave with offset)
    y_offset = -20  # Start above neutral
    y_amplitude = 30
    y_values = [y_offset + y_amplitude * math.sin(i/3) for i in range(len(x_values))]
    
    for x, y in zip(x_values, y_values):
        print(f"Target: ({x}mm, {round(y,1)}mm)")
        angles = calculate_ik(x, y)
        if angles:
            move_leg(angles[0], angles[1], 0.3)
        time.sleep(0.1)

if __name__ == "__main__":
    setup_servos()
    print("Starting wave movement (Ctrl+C to stop)")
    
    try:
        while True:
            wave_movement()
    except KeyboardInterrupt:
        setup_servos()
        print("\nMovement stopped - servos returned to neutral")
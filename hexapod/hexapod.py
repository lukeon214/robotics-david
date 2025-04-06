from adafruit_servokit import ServoKit
import time
import math

# Initialize servos
kit = ServoKit(channels=16)

# Leg configuration
L1 = 110  # mm (body to knee)
L2 = 150  # mm (knee to foot)
SERVO0_NEUTRAL = 90   # Body joint default
SERVO1_NEUTRAL = 140  # Knee joint default

def setup_servos():
    kit.servo[0].angle = SERVO0_NEUTRAL
    kit.servo[1].angle = SERVO1_NEUTRAL
    time.sleep(1)

def calculate_ik(x, y):
    x_cm = x / 10
    y_cm = y / 10
    L1_cm = L1 / 10
    L2_cm = L2 / 10
    
    distance = math.hypot(x_cm, y_cm)
    if distance > (L1_cm + L2_cm) or distance < abs(L1_cm - L2_cm):
        return None, None

    theta2 = math.acos((x_cm**2 + y_cm**2 - L1_cm**2 - L2_cm**2) / (2 * L1_cm * L2_cm))
    theta1 = math.atan2(y_cm, x_cm) - math.atan2(L2_cm * math.sin(theta2), L1_cm + L2_cm * math.cos(theta2))

    servo0_angle = 90 - math.degrees(theta1)
    servo1_angle = 180 - math.degrees(theta2)
    
    # Apply limits
    servo0_angle = max(0, min(180, servo0_angle))
    servo1_angle = max(0, min(180, servo1_angle))

    return round(servo0_angle, 1), round(servo1_angle, 1)

def move_leg(servo0_angle, servo1_angle, duration=0.5):
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
    """Performs a wave-like movement from high to low positions"""
    # Create a sequence of targets in a wave pattern
    base_x = [x for x in range(200, 100, -5)]  # X from 200mm to 100mm
    wave_y = [50 * math.sin(i/5) for i in range(len(base_x))]  # Sine wave pattern
    
    targets = list(zip(base_x, wave_y))
    
    for x, y in targets:
        print(f"\nMoving to ({x}mm, {round(y,1)}mm)")
        angles = calculate_ik(x, y)
        if angles:
            print(f"Servo angles: {angles}")
            move_leg(angles[0], angles[1], duration=0.3)
        else:
            print("Skipping unreachable position")
        time.sleep(0.1)

if __name__ == "__main__":
    setup_servos()
    print("Starting automatic wave movement...")
    
    try:
        while True:
            wave_movement()
            time.sleep(1)
            # Reverse wave
            print("\nReversing direction...")
            wave_movement()
            
    except KeyboardInterrupt:
        print("\nReturning to neutral position...")
        setup_servos()
        print("Movement stopped!")
from adafruit_servokit import ServoKit
import time
import math

# Initialize servos
kit = ServoKit(channels=16)

# Leg configuration
L1 = 110  # mm (body to knee)
L2 = 150  # mm (knee to foot)
SERVO0_NEUTRAL = 90   # Body joint default
SERVO1_NEUTRAL = 180  # Knee joint default

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

def move_leg(servo0_angle, servo1_angle, duration=1.0):
    current0 = kit.servo[0].angle
    current1 = kit.servo[1].angle
    steps = 20
    
    for step in range(steps):
        interp0 = current0 + (servo0_angle - current0) * (step + 1) / steps
        interp1 = current1 + (servo1_angle - current1) * (step + 1) / steps
        kit.servo[0].angle = interp0
        kit.servo[1].angle = interp1
        time.sleep(duration / steps)

# Interactive mode
if __name__ == "__main__":
    setup_servos()
    print("Hexapod Leg Control - Inverse Kinematics")
    print("Type 'exit' to quit\n")
    
    while True:
        try:
            x_input = input("Enter X coordinate (mm): ")
            if x_input.lower() == 'exit':
                break
                
            y_input = input("Enter Y coordinate (mm): ")
            if y_input.lower() == 'exit':
                break

            x = float(x_input)
            y = float(y_input)
            
            angles = calculate_ik(x, y)
            
            if angles:
                print(f"Moving to ({x}mm, {y}mm)")
                print(f"Servo angles: {angles}")
                move_leg(angles[0], angles[1])
                print("Movement complete!\n")
            else:
                print("⚠️ Target position unreachable! Try different coordinates.\n")
                
        except ValueError:
            print("⚠️ Invalid input! Please enter numbers only.\n")
        except KeyboardInterrupt:
            print("\nExiting...")
            break

    # Return to neutral position
    setup_servos()
    print("Servos returned to neutral position")
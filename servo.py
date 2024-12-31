from adafruit_servokit import ServoKit
import time
import threading
from sshkeyboard import listen_keyboard

kit = ServoKit(channels=16)

def move_servo(servo_number):
    angles = [0, 45, 90, 0]
    for angle in angles:
        kit.servo[servo_number].angle = angle
        time.sleep(5)  # Wait for 5 seconds before moving to the next angle

# Create threads for each servo movement
threads = []
for servo_number in [1, 2, 3]:
    thread = threading.Thread(target=move_servo, args=(servo_number,))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

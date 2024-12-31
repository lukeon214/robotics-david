from adafruit_servokit import ServoKit
import time
import threading

kit = ServoKit(channels=16)

def move_servo_2():
    kit.servo[2].angle = 0
    time.sleep(2)
    kit.servo[2].angle = 180
    time.sleep(2)
    kit.servo[2].angle = 90
    time.sleep(2)

def move_servo_1():
    kit.servo[1].angle = 65
    time.sleep(3)
    kit.servo[1].angle = 0

# Create threads for each servo movement
thread_2 = threading.Thread(target=move_servo_2)
thread_1 = threading.Thread(target=move_servo_1)

# Start the threads
thread_2.start()
thread_1.start()

# Wait for both threads to complete
thread_2.join()
thread_1.join()

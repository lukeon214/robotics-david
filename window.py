from adafruit_servokit import ServoKit
import tkinter as tk
from tkinter import messagebox

kit = ServoKit(channels=16)

def set_servo_angle(pin, angle):
    try:
        kit.servo[pin].angle = angle
        result_label.config(text=f"Servo on pin {pin} set to {angle} degrees.")
    except Exception as e:
        result_label.config(text=f"Unexpected error: {e}")

# Function to handle button click
def on_submit():
    try:
        pin = int(pin_entry.get())
        angle = int(angle_entry.get())
        set_servo_angle(pin, angle)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for pin and angle.")

# Create the main window
root = tk.Tk()
root.title("Robotic Arm Controller")
root.geometry("300x200")

# Create and place widgets
pin_label = tk.Label(root, text="Pin:")
pin_label.grid(row=0, column=0, padx=10, pady=10)

pin_entry = tk.Entry(root)
pin_entry.grid(row=0, column=1, padx=10, pady=10)

angle_label = tk.Label(root, text="Angle:")
angle_label.grid(row=1, column=0, padx=10, pady=10)

angle_entry = tk.Entry(root)
angle_entry.grid(row=1, column=1, padx=10, pady=10)

submit_button = tk.Button(root, text="Enter", command=on_submit)
submit_button.grid(row=2, column=0, columnspan=2, pady=20)

result_label = tk.Label(root, text="", fg="blue")
result_label.grid(row=3, column=0, columnspan=2)

# Run the main event loop
root.mainloop()

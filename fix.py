from gpiozero import LED

# Create an LED device using a valid pin
red = LED(17)  # Replace this with the actual pin you're using
try:
    red.blink()
except Exception as e:
    print(f"An error occurred: {str(e)}")
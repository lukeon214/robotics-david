from gpiozero import LED

while True:
    red = LED(20)
    red.blink()
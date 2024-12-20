from gpiozero import LED

while True:
    red = LED(17)
    red.blink
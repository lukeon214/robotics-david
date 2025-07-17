import time
import RPi.GPIO as GPIO
from nrf24simple import NRF24  # Use the local module

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

LED_PIN = 18
GPIO.setup(LED_PIN, GPIO.OUT)

radio = NRF24()
radio.begin(spi_bus=0, spi_device=0, ce=17)  # Match wiring: CE on GPIO17

radio.setPayloadSize(32)
radio.set_channel(0x76)
radio.setDataRate(1)
radio.setPALevel(0)

# Simple 5-byte address (must match sender)
pipe = [0xF0, 0xF0, 0xF0, 0xF0, 0xE1]
radio.openReadingPipe(1, pipe)
radio.startListening()

while True:
    if radio.available():
        received = []
        radio.read(received, 32)
        message = "".join([chr(n) for n in received if 0 < n < 128])
        print("Received:", message)

        if message.strip() == "TURNON":
            GPIO.output(LED_PIN, GPIO.HIGH)
        else:
            GPIO.output(LED_PIN, GPIO.LOW)

    time.sleep(0.5)

import time
import RPi.GPIO as GPIO
import spidev
from nrf24simple import NRF24  # Using the downloaded minimal driver

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

LED_PIN = 18
GPIO.setup(LED_PIN, GPIO.OUT)

pipes = [b"1Node", b"2Node"]  # Must match transmitter

# Setup SPI and NRF
radio = NRF24()
radio.begin(0, 0, 17)  # SPI0, CE=17 (adjust to match your wiring)
radio.setPayloadSize(32)
radio.setChannel(0x76)
radio.setDataRate(NRF24.BR_1MBPS)
radio.setPALevel(NRF24.PA_LOW)
radio.openReadingPipe(1, pipes[0])
radio.startListening()

while True:
    if radio.available():
        received = []
        radio.read(received, 32)
        message = "".join([chr(n) for n in received if n > 0])
        print("Received:", message)

        if message.strip() == "TURNON":
            GPIO.output(LED_PIN, GPIO.HIGH)
        else:
            GPIO.output(LED_PIN, GPIO.LOW)

    time.sleep(0.5)

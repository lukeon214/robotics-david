import RPi.GPIO as GPIO
from nrf24simple import NRF24
import time

# Setup
GPIO.setmode(GPIO.BCM)
LED_PIN = 17
GPIO.setup(LED_PIN, GPIO.OUT)

radio = NRF24()
radio.begin(spi_bus=0, spi_device=0, ce=25)  # CE = GPIO25, change if needed

# Set NRF24 settings
radio.setPayloadSize(32)
radio.setChannel(0x76)
radio.setDataRate(NRF24.BR_1MBPS)
radio.setPALevel(NRF24.PA_MIN)
radio.setAutoAck(True)

# Set receive address
pipes = [[0xE8, 0xE8, 0xF0, 0xF0, 0xE1]]
radio.openReadingPipe(1, pipes[0])
radio.startListening()

print("Listening for messages...")

try:
    while True:
        if radio.available():
            received = []
            radio.read(received)
            message = ''.join([chr(n) for n in received if 32 <= n <= 126])  # Clean string
            print(f"Received: {message}")

            if "on" in message.lower():
                GPIO.output(LED_PIN, GPIO.HIGH)
            elif "off" in message.lower():
                GPIO.output(LED_PIN, GPIO.LOW)

        time.sleep(0.2)

except KeyboardInterrupt:
    print("Exiting.")
    GPIO.cleanup()

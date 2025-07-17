import time
import RPi.GPIO as GPIO
from nrf24simple import NRF24

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

radio = NRF24()
radio.begin(spi_bus=0, spi_device=0, ce=17)  # Match wiring

radio.setPayloadSize(32)
radio.set_channel(0x76)
radio.setDataRate(1)
radio.setPALevel(0)

pipe = [0xF0, 0xF0, 0xF0, 0xF0, 0xE1]
radio.openReadingPipe(1, pipe)  # Not strictly needed for write, but safe
GPIO.output(radio.cePin, GPIO.LOW)  # Stop listening before writing

def send_message(msg):
    # Pad or truncate to 32 bytes
    msg = list(msg.encode("utf-8"))
    while len(msg) < 32:
        msg.append(0)
    msg = msg[:32]

    # Write payload
    radio.spi.xfer2([0xA0] + msg)
    print("Sent:", ''.join(chr(b) for b in msg if b > 0))

while True:
    send_message("TURNON")
    time.sleep(5)

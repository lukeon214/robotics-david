import time
import RPi.GPIO as GPIO
import pigpio
from nrf24 import NRF24

# Setup GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

LED_PIN = 18
GPIO.setup(LED_PIN, GPIO.OUT)

# Setup pigpio and NRF24
pi = pigpio.pi()
if not pi.connected:
    print("Could not connect to pigpio daemon")
    exit()

# Use GPIO25 for CE, GPIO8 (CE0) for CSN
radio = NRF24(pi, ce=25, csn=8)  # Adjust pins if needed

pipes = [[0xF0, 0xF0, 0xF0, 0xF0, 0xE1], [0xF0, 0xF0, 0xF0, 0xF0, 0xD2]]
radio.set_payload_size(32)
radio.set_channel(0x76)
radio.set_data_rate(NRF24.BR_1MBPS)
radio.set_pa_level(NRF24.PA_MIN)
radio.open_reading_pipe(1, pipes[0])
radio.start_listening()

# Listen and toggle LED
while True:
    if radio.available():
        received = []
        radio.read(received, radio.get_dynamic_payload_size())
        message = "".join([chr(n) for n in received if 0 < n < 128])
        print("Received:", message)

        if message.strip() == "TURNON":
            GPIO.output(LED_PIN, GPIO.HIGH)
        else:
            GPIO.output(LED_PIN, GPIO.LOW)

    time.sleep(1)

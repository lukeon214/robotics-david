import time
import pigpio
from nrf24 import NRF24

# Connect to pigpio
pi = pigpio.pi()
if not pi.connected:
    raise RuntimeError("Could not connect to pigpio daemon")

# Set up NRF24L01+
radio = NRF24(pi, ce=25)  # CE=GPIO25, CSN=GPIO8 (CE0)
radio.set_payload_size(32)
radio.set_channel(76)

# Set reading pipe address
radio.open_reading_pipe(1, b"2Node")

# Enable listening mode
radio.listen = True

print("Listening for messages...")

try:
    while True:
        if radio.data_ready():
            payload = radio.get_data()
            message = payload.decode('utf-8').rstrip('\x00')
            print("Received:", message)
        time.sleep(0.01)

except KeyboardInterrupt:
    print("Stopped by user")

finally:
    radio.listen = False
    pi.stop()

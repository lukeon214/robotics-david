import time
import pigpio
from nrf24 import NRF24

pi = pigpio.pi()
if not pi.connected:
    raise RuntimeError("Could not connect to pigpio daemon")

radio = NRF24(pi, ce=25, spi_channel=0)
radio.set_payload_size(32)
radio.set_channel(76)
radio.open_reading_pipe(1, b"2Node")

# listen = True  → start_listening()
radio.listen = True

print("Listening for messages…")
try:
    while True:
        # data_ready() stays the same
        if radio.data_ready():
            # get_data() → read()
            payload = radio.read()
            message = payload.decode("utf-8").rstrip("\x00")
            print("Received:", message)
        time.sleep(0.01)
except KeyboardInterrupt:
    print("Stopped by user")
finally:
    radio.stop_listening()
    pi.stop()

import time
import pigpio
from nrf24 import NRF24

pi = pigpio.pi()
if not pi.connected:
    raise RuntimeError("Could not connect to pigpio daemon")

radio = NRF24(pi, ce=22, spi_channel=0)
radio.set_payload_size(32)
radio.set_channel(76)
radio.open_reading_pipe(1, b"2Node")

# start_listening(), not radio.listen = True
radio.listen = True

print("Listening for messages…")

try:
    while True:
        if radio.data_ready():
            # get_payload() instead of read()/get_data()
            payload = radio.get_payload()
            message = bytes(payload).decode('utf-8').rstrip('\x00')
            print("Received:", message)
        time.sleep(0.01)

except KeyboardInterrupt:
    print("Stopped by user")

finally:
    radio.listen = False
    pi.stop()

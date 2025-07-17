import time
import pigpio
from nrf24 import NRF24

pi = pigpio.pi()
radio = NRF24(pi, ce=22, spi_channel=0)

radio.set_payload_size(32)
radio.set_channel(76)
radio.open_writing_pipe(b"1Node")
radio.open_reading_pipe(1, b"2Node")

count = 0
try:
    while True:
        msg = f"Hi {count}".encode("utf-8")
        print("Sending:", msg)
        # write() → send()
        success = radio.send(msg)
        print("Sent" if success else "Failed")
        count += 1
        time.sleep(1)
except KeyboardInterrupt:
    pass
finally:
    pi.stop()

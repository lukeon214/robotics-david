import time
import pigpio
from nrf24 import NRF24

pi = pigpio.pi()
radio = NRF24(pi, ce=22, spi_channel=0)

radio.set_payload_size(32)
radio.set_channel(76)

radio.open_writing_pipe(b"1Node")
radio.open_reading_pipe(1, b"2Node")

try:
    count = 0
    while True:
        msg = f"Hi {count}"
        print("Sending:", msg)
        success = radio.write(msg.encode('utf-8'))
        print("Sent" if success else "Failed")
        time.sleep(1)
        count += 1
except KeyboardInterrupt:
    pass
finally:
    pi.stop()

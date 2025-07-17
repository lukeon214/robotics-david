import time
import pigpio
from nrf24 import NRF24

pi = pigpio.pi()
radio = NRF24(pi, ce=22, csn=8, spi_channel=0, spi_speed=1000000)

radio.set_payload_size(32)
radio.set_channel(76)
radio.set_auto_ack(True)
radio.enable_ack_payload()
radio.set_data_rate(NRF24.DATA_RATE_1MBPS)
radio.set_pa_level(NRF24.PA_MIN)

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

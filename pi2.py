import time
import pigpio
from nrf24 import NRF24

# Connect to pigpio
pi = pigpio.pi()
if not pi.connected:
    raise RuntimeError("Could not connect to pigpio daemon")

# Setup nRF24L01
radio = NRF24(pi, ce=22, csn=8, spi_channel=0, spi_speed=1000000)

radio.set_payload_size(32)
radio.set_channel(76)
radio.set_auto_ack(True)
radio.enable_ack_payload()
radio.set_data_rate(NRF24.DATA_RATE_1MBPS)
radio.set_pa_level(NRF24.PA_MIN)

# RX address (must match TX's "writing pipe")
radio.open_reading_pipe(1, b"2Node")
radio.start_listening()

print("Waiting for messages...")

try:
    while True:
        if radio.data_ready():
            payload = radio.get_data()
            message = payload.decode('utf-8').rstrip('\x00')
            print("Received:", message)
        time.sleep(0.01)

except KeyboardInterrupt:
    print("Exiting...")

finally:
    radio.stop_listening()
    pi.stop()

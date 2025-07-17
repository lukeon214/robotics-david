import time
import pigpio
from nrf24 import NRF24

pi = pigpio.pi()

if not pi.connected:
    exit()

# NRF24L01 Setup
nrf = NRF24(pi, ce=25, payload_size=32, channel=76, data_rate=NRF24.BR_1MBPS)
nrf.set_t_address(b"2Node")
nrf.set_r_address(b"1Node")
nrf.listen = True

try:
    print("Waiting for messages...")
    while True:
        if nrf.data_ready():
            msg = nrf.get_data().decode('utf-8')
            print("Received:", msg)
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Exiting...")

finally:
    nrf.power_down()
    pi.stop()

import time
import pigpio
from nrf24 import NRF24

pi = pigpio.pi()

if not pi.connected:
    exit()

# NRF24L01 Setup
nrf = NRF24(pi, ce=25, payload_size=32, channel=76, data_rate=NRF24.BR_1MBPS)
nrf.set_t_address(b"1Node")
nrf.set_r_address(b"2Node")

try:
    count = 0
    while True:
        msg = f"Hello {count}"
        print("Sending:", msg)
        success = nrf.send(msg.encode('utf-8'))
        print("Success" if success else "Failed")
        count += 1
        time.sleep(1)

except KeyboardInterrupt:
    print("Exiting...")

finally:
    nrf.power_down()
    pi.stop()

import time
import pigpio
from nrf24 import NRF24, RF24_PAYLOAD, RF24_DATA_RATE, RF24_PA

pi = pigpio.pi()
if not pi.connected:
    raise RuntimeError("cannot connect to pigpio")

nrf = NRF24(pi,
           ce=25,
           payload_size=RF24_PAYLOAD.DYNAMIC,
           channel=76,
           data_rate=RF24_DATA_RATE.RATE_1MBPS,
           pa_level=RF24_PA.LOW)

address = "1NODE"
nrf.set_address_bytes(len(address))
nrf.open_writing_pipe(address)

count = 0
try:
    while True:
        msg = f"Hi {count}"
        print("Sending:", msg)
        # this returns True/False
        success = nrf.write(msg.encode("utf-8"))
        print("OK" if success else "FAIL")
        count += 1
        time.sleep(1)
except KeyboardInterrupt:
    pass
finally:
    pi.stop()

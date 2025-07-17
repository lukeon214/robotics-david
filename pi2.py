import time
import pigpio
from nrf24 import NRF24, RF24_PAYLOAD, RF24_DATA_RATE, RF24_PA, RF24_RX_ADDR

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
nrf.open_reading_pipe(RF24_RX_ADDR.P1, address)

# dump registers so you can verify pipe‑0 address, channel, etc.
nrf.show_registers()

nrf.listen = True

print("Listening…")
try:
    while True:
        if nrf.data_ready():
            payload = nrf.get_payload()            # returns list of ints
            text    = bytes(payload).rstrip(b'\x00').decode("utf-8")
            print("Received:", text)
        time.sleep(0.01)
except KeyboardInterrupt:
    pass
finally:
    pi.stop()

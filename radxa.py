import time
from nrf24simplee import NRF24

# Initialize NRF24 module
radio = NRF24()
radio.begin(spi_bus=0, spi_device=0, ce=24)  # CE is on GPIO17, adjust if needed

radio.setPayloadSize(32)
radio.set_channel(0x76)
radio.setDataRate(1)      # 1Mbps
radio.setPALevel(0)       # Low power

# Set the pipe address (must match Raspberry Pi receiver)
pipe = [0xF0, 0xF0, 0xF0, 0xF0, 0xE1]
radio.openReadingPipe(1, pipe)
radio.stopListening()     # Put module in TX mode

# Function to send the message
def send_message(msg):
    msg = list(msg.encode("utf-8"))
    while len(msg) < 32:
        msg.append(0)
    msg = msg[:32]

    radio.spi.xfer2([0xA0] + msg)  # 0xA0 = W_TX_PAYLOAD
    print("Sent:", ''.join(chr(b) for b in msg if b > 0))

# Main loop — send TURNON every 5 seconds
while True:
    send_message("TURNON")
    time.sleep(5)

from nrf24 import NRF24
import time
import spidev
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

pipes = [[0xF0,0xF0,0xF0,0xF0,0xE1], [0xF0,0xF0,0xF0,0xF0,0xD2]]

radio = NRF24()
radio.begin(0, 17)  # CE pin, CSN pin (adjust for your board)
radio.setPayloadSize(32)
radio.setChannel(0x76)
radio.setDataRate(NRF24.BR_1MBPS)
radio.setPALevel(NRF24.PA_MIN)
radio.openWritingPipe(pipes[0])
radio.stopListening()

message = list("TURNON")
while len(message) < 32:
    message.append(0)

while True:
    radio.write(message)
    print("Sent: TURNON")
    time.sleep(5)

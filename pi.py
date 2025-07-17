from nrf24 import NRF24
import time
import spidev
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

LED_PIN = 18
GPIO.setup(LED_PIN, GPIO.OUT)

pipes = [[0xF0,0xF0,0xF0,0xF0,0xE1], [0xF0,0xF0,0xF0,0xF0,0xD2]]

radio = NRF24()
radio.begin(0, 17)  # CE pin, CSN pin
radio.setPayloadSize(32)
radio.setChannel(0x76)
radio.setDataRate(NRF24.BR_1MBPS)
radio.setPALevel(NRF24.PA_MIN)
radio.openReadingPipe(1, pipes[0])
radio.startListening()

while True:
    if radio.available():
        received = []
        radio.read(received, radio.getDynamicPayloadSize())
        message = "".join([chr(n) for n in received if n != 0])
        print("Received:", message)

        if message.strip() == "TURNON":
            GPIO.output(LED_PIN, GPIO.HIGH)
        else:
            GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(1)

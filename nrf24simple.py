import RPi.GPIO as GPIO
import spidev
import time

class NRF24:
    def __init__(self):
        self.cePin = 17
        self.csnPin = 0
        self.payload_size = 32
        self.channel = 76
        self.spi = spidev.SpiDev()

    def begin(self, spi_bus=0, spi_device=0, ce=17):
        self.cePin = ce
        GPIO.setup(self.cePin, GPIO.OUT)
        GPIO.output(self.cePin, GPIO.LOW)
        self.spi.open(spi_bus, spi_device)
        self.spi.max_speed_hz = 4000000
        self.spi.mode = 0
        self.config_radio()

    def config_radio(self):
        self.write_register(0x00, 0x0F)  # CONFIG
        self.set_channel(self.channel)
        self.setPayloadSize(self.payload_size)
        self.setDataRate(1)
        self.setPALevel(0)
        time.sleep(0.1)
        GPIO.output(self.cePin, GPIO.HIGH)

    def write_register(self, reg, value):
        self.spi.xfer2([0x20 | reg, value])

    def read_register(self, reg):
        return self.spi.xfer2([reg, 0x00])[1]

    def set_channel(self, ch):
        self.channel = ch
        self.write_register(0x05, ch)

    def setPayloadSize(self, size):
        self.payload_size = size
        self.write_register(0x11, size)

    def setDataRate(self, rate):
        if rate == 1:
            self.write_register(0x06, 0x06)  # 1Mbps
        elif rate == 2:
            self.write_register(0x06, 0x07)  # 2Mbps

    def setPALevel(self, level):
        levels = [0x00, 0x02, 0x04, 0x06]
        self.write_register(0x06, levels[level])

    def openReadingPipe(self, pipe, address):
        self.write_register(0x0A + pipe, address[0])
        self.write_register(0x0B + pipe, address[1])
        self.write_register(0x0C + pipe, address[2])
        self.write_register(0x0D + pipe, address[3])
        self.write_register(0x0E + pipe, address[4])

    def startListening(self):
        GPIO.output(self.cePin, GPIO.HIGH)

    def available(self):
        return bool(self.read_register(0x17) & 0x40)

    def read(self, buffer, length):
        data = self.spi.xfer2([0x61] + [0x00]*length)[1:]
        buffer.clear()
        buffer.extend(data)

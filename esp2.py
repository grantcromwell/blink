from machine import UART, Pin, I2C
from time import sleep

uartSender = UART(1, baudrate=9600, tx=Pin(43), rx=Pin(44))
sda = Pin(11)
scl = Pin(12)
i2c = I2C(0, scl=scl, sda=sda, freq=100000)

print(i2c.scan())

        

while True:
    uartSender.write(b'0\n')
    sleep(0.5)

    uartSender.write(b'1\n')
    sleep(0.5)

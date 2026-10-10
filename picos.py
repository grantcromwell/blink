from machine import UART, Pin, I2C
from time import sleep

uartSender = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))
picoSender = UART(1, baudrate=115200, tx=Pin(4), rx=Pin(5))


while True:
    uartSender.write(b'0\n')
    picoSender.write(b'0\n')
    sleep(0.5)

    uartSender.write(b'1\n')
    picoSender.write(b'1\n')
    sleep(0.5)


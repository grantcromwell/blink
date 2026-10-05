import machine
from machine import UART, Pin
from time import sleep

uartSender = UART(1, baudrate=9600, tx=Pin(43), rx=Pin(44))

while True:
    uartSender.write(b'ON\n')
    sleep(2.3)
    
    uartSender.write(b'OFF\n')
    sleep(2.3)

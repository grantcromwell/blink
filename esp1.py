from machine import UART, Pin
from time import sleep

led = Pin(48, Pin.OUT)
uartRecv = UART(1, baudrate=9600, tx=Pin(43), rx=Pin(44))

buffer = b''

while True:
    if uartRecv.any():
        chunk = uartRecv.read()
        if chunk:
            buffer += chunk
    while b'\n' in buffer:
        currentmsg, buffer = buffer.split(b'\n', 1)
        msg = currentmsg.decode().strip()
        print(repr(msg))
        
        if msg == '1':
            led.value(1)
            
        elif msg == '0':
            led.value(0)

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
        rawmsg, buffer = buffer.split(b'\n', 1)
        msg = rawmsg.decode().strip()
        print(repr(msg))
        
        if msg == 'ON':
            led.value(1)
            
        elif msg == 'OFF':
            led.value(0)

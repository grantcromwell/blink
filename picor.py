from machine import UART, Pin
from time import sleep


led = Pin("LED", Pin.OUT)
uartRecv = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))



buffer = b''

while True:
    if uartRecv.any():
        print("recver running")
        chunk = uartRecv.read()
        if chunk:
            buffer += chunk
    while b'\n' in buffer:
        currentmsg, buffer = buffer.split(b'\n', 1)
        msg = currentmsg.decode().strip()
        print(repr(msg))
        
        if msg == '1':
            led.on()
            
            
        elif msg == '0':
            led.off()
           


from machine import Pin, I2C, UART
import ssd1306

WIDTH = 128
HEIGHT = 64
DISPLAY_ADDR = 0x3C

uartrecv = UART(0, baudrate=115200, rx=Pin(1))

i2c = I2C(1, sda=Pin(6), scl=Pin(7), freq=200000)
display = ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3C)


buffer = b''

while True:
    if uartrecv.any():
        print("Pico UART0 initialized: 115200 baud, TX=GP0, RX=GP1")
        chunk = uartrecv.read()
        if chunk:
            print("UART bytes:", repr(chunk))
            buffer += chunk
    while b'\n' in buffer:
        currentmsg, buffer = buffer.split(b'\n', 1)
        msg = currentmsg.decode().strip()
        print(repr(msg))
        
        if msg == '1':
            display.fill(0)
            display.text("1", 60, 28)
            display.show()
            
        elif msg == '0':
            display.fill(0)
            display.text("0", 60, 28)
            display.show()


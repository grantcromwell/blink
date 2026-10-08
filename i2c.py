from machine import Pin, I2C


WIDTH = 128
HEIGHT = 64
DISPLAY_ADDR = 0x3C


i2c = I2C(1, sda=Pin(6), scl=Pin(7), freq=200000)
found = i2c.scan()
print("I2C devices:", [hex(address) for address in found])

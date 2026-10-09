from machine import Pin, I2C

WIDTH = 128
HEIGHT = 64
DISPLAY_ADDR = 0x3C

i2c = I2C(1, sda=Pin(6), scl=Pin(7), freq=200000)
found = i2c.scan()
print("I2C devices:", [hex(address) for address in found])

if DISPLAY_ADDR not in found:
    raise OSError("No I2C device found at address 0x3C")


def command(value):
    i2c.writeto(DISPLAY_ADDR, bytes((0x00, value)))


for value in (
    0xAE,
    0xD5, 0x80,
    0xA8, 0x3F,
    0xD3, 0x00,
    0x40,
    0x8D, 0x14,
    0x20, 0x02,
    0xA1,
    0xC8,
    0xDA, 0x12,
    0x81, 0x7F,
    0xD9, 0xF1,
    0xDB, 0x40,
    0xA4,
    0xA6,
    0xAF,
):
    command(value)


frame = bytearray(WIDTH * HEIGHT // 8)


def pixel(x, y):
    if 0 <= x < WIDTH and 0 <= y < HEIGHT:
        index = x + (y // 8) * WIDTH
        frame[index] |= 1 << (y & 7)


def circle(cx, cy, radius):
    x = radius
    y = 0
    error = 1 - radius

    while x >= y:
        pixel(cx + x, cy + y)
        pixel(cx + y, cy + x)
        pixel(cx - y, cy + x)
        pixel(cx - x, cy + y)
        pixel(cx - x, cy - y)
        pixel(cx - y, cy - x)
        pixel(cx + y, cy - x)
        pixel(cx + x, cy - y)
        y += 1
        if error < 0:
            error += 2 * y + 1
        else:
            x -= 1
            error += 2 * (y - x) + 1


circle(WIDTH // 2, HEIGHT // 2, 20)

for page in range(HEIGHT // 8):
    command(0xB0 + page)
    command(0x00)
    command(0x10)
    start = page * WIDTH
    i2c.writeto(DISPLAY_ADDR, b"\x40" + frame[start:start + WIDTH])

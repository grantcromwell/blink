from machine import Pin, UART
from time import sleep

led = Pin(25, Pin.OUT)
uart = UART(0, baudrate=115200, tx=Pin(0), rx=Pin(1), rxbuf=512)
led.off()


def runLedCommands(message):
    if not message:
        return False

    commands = message.split(",")
    if len(commands) % 2 != 0:
        return False

    for index in range(0, len(commands), 2):
        onCommand = commands[index].split(":")
        offCommand = commands[index + 1].split(":")

        if len(onCommand) != 2 or len(offCommand) != 2:
            led.off()
            return False
        if onCommand[0] != "ON" or offCommand[0] != "OFF":
            led.off()
            return False

        try:
            onLength = float(onCommand[1])
            offLength = float(offCommand[1])
        except ValueError:
            led.off()
            return False

        if onLength <= 0 or onLength > 5 or offLength <= 0 or offLength > 5:
            led.off()
            return False

        led.on()
        sleep(onLength)
        led.off()
        sleep(offLength)

    led.off()
    return True


receivedBytes = b""

while True:
    nextByte = uart.read(1)
    if nextByte is None:
        sleep(0.001)
        continue

    if nextByte != b"\n":
        if nextByte != b"\r":
            receivedBytes += nextByte
        continue

    try:
        commands = receivedBytes.decode("ascii").strip()
    except UnicodeError:
        led.off()
        uart.write(b"ERR\n")
        receivedBytes = b""
        continue

    receivedBytes = b""
    if runLedCommands(commands):
        uart.write(b"DONE\n")
    else:
        uart.write(b"ERR\n")

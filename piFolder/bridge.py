import os
import sys
import termios


hostDevice = "/dev/[CHANGEME]"
picoDevice = "/dev/[CHANGEME]"
baud = termios.B115200

dotSeconds = 0.3
dashSeconds = dotSeconds * 3
elementGapSeconds = dotSeconds
letterGapSeconds = dotSeconds * 3


def configureSerial(descriptor, timeoutSeconds=0):
    settings = termios.tcgetattr(descriptor)

    settings[2] = termios.CS8 | termios.CREAD | termios.CLOCAL
    settings[6][termios.VMIN] = 0 if timeoutSeconds else 1
    settings[6][termios.VTIME] = timeoutSeconds * 10
    settings[4] = baud
    settings[5] = baud
    settings[0] = 0
    settings[1] = 0
    settings[3] = 0

    termios.tcsetattr(descriptor, termios.TCSANOW, settings)


def readBytes(descriptor):
    receivedBytes = b""

    while True:
        nextByte = os.read(descriptor, 1)
        if nextByte == b"":
            raise TimeoutError("Pico UART response timed out")
        if nextByte == b"\n":
            return receivedBytes.strip()
        if nextByte != b"\r":
            receivedBytes += nextByte


def writeLine(descriptor, message):
    messageBytes = message.encode("ascii") + b"\n"
    sentBytes = 0

    while sentBytes < len(messageBytes):
        sentBytes += os.write(descriptor, messageBytes[sentBytes:])


def sendPhases(picoDescriptor, phases):
    termios.tcflush(picoDescriptor, termios.TCIFLUSH)
    writeLine(picoDescriptor, ",".join(phases))
    responseBytes = readBytes(picoDescriptor)
    response = responseBytes.decode("ascii")

    if response != "DONE":
        raise RuntimeError("Pico did not finish the LED phases")
    print("Pico: " + response, flush=True)


def main():
    hostDescriptor = os.open(hostDevice, os.O_RDWR | os.O_NOCTTY)
    picoDescriptor = os.open(picoDevice, os.O_RDWR | os.O_NOCTTY)

    try:
        configureSerial(hostDescriptor)
        configureSerial(picoDescriptor, 10)
        print("Bridge ready", flush=True)

        while True:
            requestBytes = os.read(hostDescriptor, 1)
            if not requestBytes:
                raise ConnectionError("Host USB serial disconnected")

            response = requestBytes.decode("ascii", errors="ignore").lower()
            print(response, flush=True)

            hexadecimalCode = hashTable.get(response)
            blinkFunction = hexToFunction.get(hexadecimalCode)
            if blinkFunction is None:
                continue

            try:
                blinkFunction(picoDescriptor)
            except Exception as error:
                print("Pico request failed: " + str(error), file=sys.stderr)
    finally:
        os.close(hostDescriptor)
        os.close(picoDescriptor)




hashTable = {
    "a": "1a01",
    "b": "1a02",
    "c": "1a03",
    "d": "1a04",
    "e": "1a05",
    "f": "1a06",
    "g": "1a07",
    "h": "1a08",
    "i": "1a09",
    "j": "1a10",
    "k": "1a11",
    "l": "1a12",
    "m": "1a13",
    "n": "1a14",
    "o": "1a15",
    "p": "1a16",
    "q": "1a17",
    "r": "1a18",
    "s": "1a19",
    "t": "1a20",
    "u": "1a21",
    "v": "1a22",
    "w": "1a23",
    "x": "1a24",
    "y": "1a25",
    "z": "1a26",
    "0": "2a00",
    "1": "2a01",
    "2": "2a02",
    "3": "2a03",
    "4": "2a04",
    "5": "2a05",
    "6": "2a06",
    "7": "2a07",
    "8": "2a08",
    "9": "2a09",
}


def blink1a01(picoDescriptor):
    phases = [
        "ON:" + str(dotSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dashSeconds),
        "OFF:" + str(letterGapSeconds),
    ]
    sendPhases(picoDescriptor, phases)

def blink1a02(picoDescriptor):
    phases = [
        "ON:" + str(dashSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dotSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dotSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dotSeconds),
        "OFF:" + str(letterGapSeconds),
    ]
    sendPhases(picoDescriptor, phases)

def blink1a03(picoDescriptor):
    phases = [
        "ON:" + str(dashSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dotSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dashSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dotSeconds),
        "OFF:" + str(letterGapSeconds),
    ]
    sendPhases(picoDescriptor, phases)

def blink1a04(picoDescriptor):
    phases = [
        "ON:" + str(dashSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dotSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dotSeconds),
        "OFF:" + str(letterGapSeconds),
    ]
    sendPhases(picoDescriptor, phases)

def blink1a05(picoDescriptor):
    phases = [
        "ON:" + str(dotSeconds),
        "OFF:" + str(letterGapSeconds),
    ]
    sendPhases(picoDescriptor, phases)

def blink1a06(picoDescriptor):
    phases = [
        "ON:" + str(dotSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dotSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dashSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dotSeconds),
        "OFF:" + str(letterGapSeconds),
    ]
    sendPhases(picoDescriptor, phases)

def blink1a07(picoDescriptor):
    phases = [
        "ON:" + str(dashSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dashSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dotSeconds),
        "OFF:" + str(letterGapSeconds),
    ]
    sendPhases(picoDescriptor, phases)

def blink1a08(picoDescriptor):
    phases = [
        "ON:" + str(dotSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dotSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dotSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dotSeconds),
        "OFF:" + str(letterGapSeconds),
    ]
    sendPhases(picoDescriptor, phases)

def blink1a09(picoDescriptor):
    phases = [
        "ON:" + str(dotSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dotSeconds),
        "OFF:" + str(letterGapSeconds),
    ]
    sendPhases(picoDescriptor, phases)

def blink1a10(picoDescriptor):
    phases = [
        "ON:" + str(dotSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dashSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dashSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dashSeconds),
        "OFF:" + str(letterGapSeconds),
    ]
    sendPhases(picoDescriptor, phases)

def blink1a11(picoDescriptor):
    phases = [
        "ON:" + str(dashSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dotSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dashSeconds),
        "OFF:" + str(letterGapSeconds),
    ]
    sendPhases(picoDescriptor, phases)

def blink1a12(picoDescriptor):
    phases = [
        "ON:" + str(dotSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dashSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dotSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dotSeconds),
        "OFF:" + str(letterGapSeconds),
    ]
    sendPhases(picoDescriptor, phases)

def blink1a13(picoDescriptor):
    phases = [
        "ON:" + str(dashSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dashSeconds),
        "OFF:" + str(letterGapSeconds),
    ]
    sendPhases(picoDescriptor, phases)

def blink1a14(picoDescriptor):
    phases = [
        "ON:" + str(dashSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dotSeconds),
        "OFF:" + str(letterGapSeconds),
    ]
    sendPhases(picoDescriptor, phases)

def blink1a15(picoDescriptor):
    phases = [
        "ON:" + str(dashSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dashSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dashSeconds),
        "OFF:" + str(letterGapSeconds),
    ]
    sendPhases(picoDescriptor, phases)

def blink1a16(picoDescriptor):
    phases = [
        "ON:" + str(dotSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dashSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dashSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dotSeconds),
        "OFF:" + str(letterGapSeconds),
    ]
    sendPhases(picoDescriptor, phases)

def blink1a17(picoDescriptor):
    phases = [
        "ON:" + str(dashSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dashSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dotSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dashSeconds),
        "OFF:" + str(letterGapSeconds),
    ]
    sendPhases(picoDescriptor, phases)

def blink1a18(picoDescriptor):
    phases = [
        "ON:" + str(dotSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dashSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dotSeconds),
        "OFF:" + str(letterGapSeconds),
    ]
    sendPhases(picoDescriptor, phases)

def blink1a19(picoDescriptor):
    phases = [
        "ON:" + str(dotSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dotSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dotSeconds),
        "OFF:" + str(letterGapSeconds),
    ]
    sendPhases(picoDescriptor, phases)

def blink1a20(picoDescriptor):
    phases = [
        "ON:" + str(dashSeconds),
        "OFF:" + str(letterGapSeconds),
    ]
    sendPhases(picoDescriptor, phases)

def blink1a21(picoDescriptor):
    phases = [
        "ON:" + str(dotSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dotSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dashSeconds),
        "OFF:" + str(letterGapSeconds),
    ]
    sendPhases(picoDescriptor, phases)

def blink1a22(picoDescriptor):
    phases = [
        "ON:" + str(dotSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dotSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dotSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dashSeconds),
        "OFF:" + str(letterGapSeconds),
    ]
    sendPhases(picoDescriptor, phases)

def blink1a23(picoDescriptor):
    phases = [
        "ON:" + str(dotSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dashSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dashSeconds),
        "OFF:" + str(letterGapSeconds),
    ]
    sendPhases(picoDescriptor, phases)

def blink1a24(picoDescriptor):
    phases = [
        "ON:" + str(dashSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dotSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dotSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dashSeconds),
        "OFF:" + str(letterGapSeconds),
    ]
    sendPhases(picoDescriptor, phases)

def blink1a25(picoDescriptor):
    phases = [
        "ON:" + str(dashSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dotSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dashSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dashSeconds),
        "OFF:" + str(letterGapSeconds),
    ]
    sendPhases(picoDescriptor, phases)

def blink1a26(picoDescriptor):
    phases = [
        "ON:" + str(dashSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dashSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dotSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dotSeconds),
        "OFF:" + str(letterGapSeconds),
    ]
    sendPhases(picoDescriptor, phases)

def blink2a00(picoDescriptor):
    phases = [
        "ON:" + str(dashSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dashSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dashSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dashSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dashSeconds),
        "OFF:" + str(letterGapSeconds),
    ]
    sendPhases(picoDescriptor, phases)

def blink2a01(picoDescriptor):
    phases = [
        "ON:" + str(dotSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dashSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dashSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dashSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dashSeconds),
        "OFF:" + str(letterGapSeconds),
    ]
    sendPhases(picoDescriptor, phases)

def blink2a02(picoDescriptor):
    phases = [
        "ON:" + str(dotSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dotSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dashSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dashSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dashSeconds),
        "OFF:" + str(letterGapSeconds),
    ]
    sendPhases(picoDescriptor, phases)

def blink2a03(picoDescriptor):
    phases = [
        "ON:" + str(dotSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dotSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dotSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dashSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dashSeconds),
        "OFF:" + str(letterGapSeconds),
    ]
    sendPhases(picoDescriptor, phases)

def blink2a04(picoDescriptor):
    phases = [
        "ON:" + str(dotSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dotSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dotSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dotSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dashSeconds),
        "OFF:" + str(letterGapSeconds),
    ]
    sendPhases(picoDescriptor, phases)

def blink2a05(picoDescriptor):
    phases = [
        "ON:" + str(dotSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dotSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dotSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dotSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dotSeconds),
        "OFF:" + str(letterGapSeconds),
    ]
    sendPhases(picoDescriptor, phases)

def blink2a06(picoDescriptor):
    phases = [
        "ON:" + str(dashSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dotSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dotSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dotSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dotSeconds),
        "OFF:" + str(letterGapSeconds),
    ]
    sendPhases(picoDescriptor, phases)

def blink2a07(picoDescriptor):
    phases = [
        "ON:" + str(dashSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dashSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dotSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dotSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dotSeconds),
        "OFF:" + str(letterGapSeconds),
    ]
    sendPhases(picoDescriptor, phases)

def blink2a08(picoDescriptor):
    phases = [
        "ON:" + str(dashSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dashSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dashSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dotSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dotSeconds),
        "OFF:" + str(letterGapSeconds),
    ]
    sendPhases(picoDescriptor, phases)

def blink2a09(picoDescriptor):
    phases = [
        "ON:" + str(dashSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dashSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dashSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dashSeconds),
        "OFF:" + str(elementGapSeconds),
        "ON:" + str(dotSeconds),
        "OFF:" + str(letterGapSeconds),
    ]
    sendPhases(picoDescriptor, phases)


hexToFunction = {
    "1a01": blink1a01,
    "1a02": blink1a02,
    "1a03": blink1a03,
    "1a04": blink1a04,
    "1a05": blink1a05,
    "1a06": blink1a06,
    "1a07": blink1a07,
    "1a08": blink1a08,
    "1a09": blink1a09,
    "1a10": blink1a10,
    "1a11": blink1a11,
    "1a12": blink1a12,
    "1a13": blink1a13,
    "1a14": blink1a14,
    "1a15": blink1a15,
    "1a16": blink1a16,
    "1a17": blink1a17,
    "1a18": blink1a18,
    "1a19": blink1a19,
    "1a20": blink1a20,
    "1a21": blink1a21,
    "1a22": blink1a22,
    "1a23": blink1a23,
    "1a24": blink1a24,
    "1a25": blink1a25,
    "1a26": blink1a26,
    "2a00": blink2a00,
    "2a01": blink2a01,
    "2a02": blink2a02,
    "2a03": blink2a03,
    "2a04": blink2a04,
    "2a05": blink2a05,
    "2a06": blink2a06,
    "2a07": blink2a07,
    "2a08": blink2a08,
    "2a09": blink2a09,
}


if __name__ == "__main__":
    raise SystemExit(main())

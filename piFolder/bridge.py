import os
import termios
import sys


hostDevice = os.environ["bridgeHost"]
picoDevice = os.environ["bridgePico"]
baud = termios.B9600

dotSeconds = 0.3
dashSeconds = dotSeconds * 3
elementGapSeconds = dotSeconds
letterGapSeconds = dotSeconds * 3


morseCode = {
    0x41: ".-", 0x42: "-...", 0x43: "-.-.", 0x44: "-..", 0x45: ".",
    0x46: "..-.", 0x47: "--.", 0x48: "....", 0x49: "..", 0x4a: ".---",
    0x4b: "-.-", 0x4c: ".-..", 0x4d: "--", 0x4e: "-.", 0x4f: "---",
    0x50: ".--.", 0x51: "--.-", 0x52: ".-.", 0x53: "...", 0x54: "-",
    0x55: "..-", 0x56: "...-", 0x57: ".--", 0x58: "-..-", 0x59: "-.--",
    0x5a: "--..", 0x30: "-----", 0x31: ".----", 0x32: "..---",
    0x33: "...--", 0x34: "....-", 0x35: ".....", 0x36: "-....",
    0x37: "--...", 0x38: "---..", 0x39: "----."
}

def configSerial(devopen):
    settings = termios.tcgetattr(devopen)
    settings[2] = termios.CS8 | termios.CREAD | termios.CLOCAL
    settings[6][termios.VMIN] = 1
    settings[6][termios.VTIME] = 0
    settings[4] = baud
    settings[5] = baud
    settings[0] = 0
    settings[1] = 0
    settings[3] = 0
    termios.tcsetattr(devopen, termios.TCSANOW, settings)


def msgWriter(devopen, msg):
    data = msg.encode("ascii") + b"\n"
    byteCounter = 0
    while byteCounter < len(data):
        byteCounter += os.write(devopen, data[byteCounter:])

def morseConverter(morse):
    blinks = []
    for blips, boop in enumerate(morse):
        bleeps = dotSeconds if boop == "." else dashSeconds
        noSound = elementGapSeconds if blips + 1 < len(morse) else letterGapSeconds
        blinks.append("On:" + str(bleeps))
        blinks.append("Off:" + str(noSound))
    return "+".join(blinks)

def morseDecoder(morse):
     dmorse = {
          code: input
          for input, code in morseCode.items()
     }
     return dmorse.get(morse)
     


host = os.open(hostDevice, os.O_RDWR | os.O_NOCTTY)
pico = os.open(picoDevice, os.O_RDWR | os.O_NOCTTY)

try:
    configSerial(host)
    configSerial(pico)

    while True:
        data = os.read(host, 1)
        if not data:
            continue
    
        morse = morseCode.get(data[0])

        if morse is not None:
            proofRead = morseDecoder(morse)
            if (proofRead != data[0]):
                        continue
            msgWriter(pico, morseConverter(morse))
        else: 
             msgWriter(host, "Stop doing that. Try again")  
finally:
    os.close(host)
    os.close(pico)




    

import os
import sys
import termios
import tty

port = os.environ["ArduinoEsp1"]


devopen = os.open(port, os.O_RDWR | os.O_NOCTTY | os.O_NONBLOCK)
try:
    attribs = termios.tcgetattr(devopen)
    attribs[4] = termios.B115200
    attribs[5] = termios.B115200
    attribs[1] = 0
    attribs[2] = 0
    attribs[3] = 0

    tty.setraw(devopen)
    termios.tcsetattr(devopen, termios.TCSANOW, attribs)
    print("Enter in a ")
    bytestream = b''

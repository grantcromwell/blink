

import os
import sys
import termios


BAUD = termios.B115200


def configureSerial(descriptor):
    settings = termios.tcgetattr(descriptor)

    settings[2] = termios.CS8 | termios.CREAD | termios.CLOCAL
    settings[6][termios.VMIN] = 0
    settings[6][termios.VTIME] = 0
    settings[4] = BAUD
    settings[5] = BAUD
    settings[0] = 0
    settings[1] = 0
    settings[3] = 0
    termios.tcsetattr(descriptor, termios.TCSANOW, settings)


def main():
    device = os.environ["emhost"]
    character = input("Press any key to start: ").upper()

    if len(character) != 1 or character not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
        print("Enter one letter A-Z or digit 0-9.")
        return 2

    descriptor = os.open(device, os.O_RDWR | os.O_NOCTTY)
    try:
        configureSerial(descriptor)
        messageBytes = character.encode("ascii")
        os.write(descriptor, messageBytes)
    finally:
        os.close(descriptor)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

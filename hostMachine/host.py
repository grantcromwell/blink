

import os
import sys
import termios
from time import sleep
import tty
 
port = os.environ["bridgePi4"]
baud = termios.B9600


devopen = os.open(port, os.O_RDWR | os.O_NOCTTY)



try: 
    settings = termios.tcgetattr(devopen)
    tty.setraw(devopen)
    settings[4] = baud
    settings[5] = baud
    termios.tcsetattr(devopen, termios.TCSANOW, settings)


    entry = input("Enter in one letter or number").upper() 

    if len(entry) != 1 or not entry.isalnum():
        print("Please enter in one letter or number!")
        return 2
    else:
        os.write(devopen, entry.encode("ascii"))
        print(f"Sending: {entry} to Pico!") 
finally:
    os.close(devopen)


    
          



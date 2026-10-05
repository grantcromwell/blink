

import os
import sys
import termios
from time import sleep
import tty
 
port = os.environ["hostDevi"]
baud = termios.B9600


devopen = os.open(port, os.O_RDWR | os.O_NOCTTY)



try: 
    settings = termios.tcgetattr(devopen)
    tty.setraw(devopen)
    settings[4] = baud
    settings[5] = baud
    termios.tcsetattr(devopen, termios.TCSANOW, settings)


    entry = print("Enter in one letter or number").Upper() 

    if len(entry) != 1 or not entry.isanum():
        print("Please enter in one letter or number!")
    else:
        os.write(devopen, entry.encode("ascii"))
        print("Sending: {entry} to Pico!") 
finally:
    os.close(devopen)


    
          



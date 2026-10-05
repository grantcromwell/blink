# Raspberry Pi Pico blinking program

from machine import Pin
from time import sleep

led = Pin(25, Pin.OUT)  

def blinkFaRep():
        for go in range(7):
                led.on()
                sleep(0.1)
                led.off()
                sleep(0.1)
                led.on()
                sleep(0.1)
                led.off()


def blinkFast():
        blinkFaRep()
        blinkFaRep()



def blinkSlow():
        for go in range(2):
                sleep(0.7)
                led.off()
                sleep(0.7)
                led.on()
                sleep(0.7)
                led.off()





while True:
   blinkFast()
   blinkSlow()

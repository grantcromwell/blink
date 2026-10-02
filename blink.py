# Raspberry Pi Pico blinking program

from machine import Pin
from time import sleep

led = Pin(25, Pin.OUT)  

def blinkFast():
        led.on()
        sleep(0.1)
        led.off()
        sleep(0.1)
        led.on()
        sleep(0.1)
        led.off()
        sleep(0.1)
        led.on()
        sleep(0.1)
        led.off()
        sleep(0.1)
        led.on()
        sleep(0.1)
        led.off()
        sleep(0.1)
        led.on()



def blinkSlow():
        sleep(0.7)
        led.off()
        sleep(0.7)
        led.on()
        sleep(0.7)
        led.off()





while True:
   blinkFast()
   blinkSlow()

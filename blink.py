from machine import Pin
from utime import sleep

onBoardLED = Pin("LED", Pin.OUT)

def blink():
    onBoardLED.toggle()
    sleep(1)

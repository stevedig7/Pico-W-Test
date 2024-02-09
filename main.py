from machine import Pin
from utime import sleep
from ota_updater import update_ota

def ota():
    onBoardLED.value(1)
    update_ota()

def blink():
    onBoardLED.toggle()
    sleep(0.1)

# –––––––––––––––––––––––––––––––––––––
onBoardLED = Pin("LED", Pin.OUT)
otaUpdatePin = Pin(5, Pin.IN, Pin.PULL_UP)

while True:
    if not otaUpdatePin.value(): ota()
    blink()
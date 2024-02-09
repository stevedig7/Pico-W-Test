from ota_updater import update_ota
from machine import Pin
from utime import sleep

def blink():
    onBoardLED.toggle()
    sleep(1)
# ––––––––––––––––––––––––––
otaUpdatePin = Pin(5, Pin.IN, Pin.PULL_UP)
onBoardLED = Pin("LED", Pin.OUT)

while True:
    if not otaUpdatePin.value():
        update_ota()
    blink()


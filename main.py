from ota_updater import update_ota
from machine import Pin
from utime import sleep

def blink():
    print('blink')
    onBoardLED.toggle()
    sleep(0.1)
# ––––––––––––––––––––––––––
otaUpdatePin = Pin(5, Pin.IN, Pin.PULL_UP)
onBoardLED = Pin("LED", Pin.OUT)

while True:
    if not otaUpdatePin.value():
        onBoardLED.value(1)
        update_ota()
    blink()
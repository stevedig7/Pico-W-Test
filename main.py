from ota_updater import update_ota
from blink import blink

otaUpdatePin = Pin(5, Pin.IN, Pin.PULL_UP)

while True:
    if not otaUpdatePin.value():
        update_ota()
    blink()
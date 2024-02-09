from machine import Pin
from utime import sleep
from ota_updater import update_ota

pin = Pin("LED", Pin.OUT)
otaUpdatePin = Pin(5, Pin.IN, Pin.PULL_UP)

print("LED starts flashing...")
while True:
    pin.toggle()
    sleep(1)

    if not otaUpdatePin.value():
        print('Updating code from GitHub')
        update_ota()

# Code 3
from machine import Pin
from utime import sleep

pin = Pin("LED", Pin.OUT)

print("LED starts flashing...")
while True:
    try:
        pin.toggle()
        sleep(0.3) # sleep 1sec
    except KeyboardInterrupt:
        break
pin.off()
print("Finished.")

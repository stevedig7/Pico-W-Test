import machine
from machine import Pin
import network
import usocket as socket
import uhttpd
import time
from SECRET import SSID, PASSWORD

# Define pin number for the LED
LED_PIN = 0  # Assuming LED is connected to Pin 0
otaUpdatePin = Pin(5, Pin.IN, Pin.PULL_UP)

# Connect to Wi-Fi
def connect_wifi():
    ssid = SSID
    password = PASSWORD
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("Connecting to WiFi...")
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            pass
    print("Connected to WiFi")
    print("IP Address:", wlan.ifconfig()[0])

# Function to handle HTTP requests
def handle_http_request(req):
    html = """<!DOCTYPE html>
    <html>
    <head>
    <title>LED Blink Frequency</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>
    <body>
    <h1>LED Blink Frequency</h1>
    <input type="range" min="1" max="10" value="1" class="slider" id="freqRange">
    <p>Blink Frequency: <span id="freqValue"></span></p>
    <script>
    var slider = document.getElementById("freqRange");
    var output = document.getElementById("freqValue");
    output.innerHTML = slider.value;

    slider.oninput = function() {
        output.innerHTML = this.value;
        var xhr = new XMLHttpRequest();
        xhr.open("GET", "/set_freq?freq=" + this.value, true);
        xhr.send();
    }
    </script>
    </body>
    </html>
    """

    if req.get("PATH_INFO") == "/":
        return uhttpd.Response(200, html)
    elif req.get("PATH_INFO") == "/set_freq":
        freq = int(req.get("QUERY_STRING").split("=")[1])
        blink_led_freq(freq)
        return uhttpd.Response(200, "Frequency set to {}".format(freq))
    else:
        return uhttpd.Response(404, "Not Found")

# Function to blink LED with specified frequency
def blink_led_freq(freq):
    led = machine.Pin(LED_PIN, machine.Pin.OUT)
    while True:
        led.value(1)  # Turn on LED
        time.sleep(1 / (2 * freq))
        led.value(0)  # Turn off LED
        time.sleep(1 / (2 * freq))
        if not otaUpdatePin.value():
            print('Updating code from GitHub')
            update_ota()

# Main function
def main():
    connect_wifi()
    server = uhttpd.Server()
    server.set_app(handle_http_request)
    server.begin()

    # Start with default frequency of 1 Hz
    blink_led_freq(1)

if __name__ == "__main__":
    main()

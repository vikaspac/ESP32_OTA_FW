"""
Vikasred
"""

##########################################################################
from ota import OTAUpdater
from WIFI_CONFIG import WIFI_SSID, WIFI_PSWD

firmware_url = "https://github.com/vikaspac/ESP32_OTA_FW/blob/main/b4fa78/"
ota_updater = OTAUpdater(WIFI_SSID, WIFI_PSWD, firmware_url, "main.py")
ota_updater.download_and_install_update_if_available()
##########################################################################


# Import the `Pin` class from the `machine` module to access hardware
from machine import Pin
import time

# Initialize LED pin (e.g., GPIO2 for ESP32 board)
led = Pin(2, Pin.OUT)

print(f"Start blinking {led}. Press `Ctrl+C` to stop")

try:
    # Forever loop to blink the LED
    while True:
        # led.value(not led.value())
        # time.sleep(0.5)
        led.on()
        print(f"LED ON")
        time.sleep(1)
        led.off()
        print(f"LED OFF")
        time.sleep(1)

except KeyboardInterrupt:
    # This part runs when Ctrl+C is pressed
    print("Program stopped. Exiting...")

    # Optional cleanup code
    led.off()

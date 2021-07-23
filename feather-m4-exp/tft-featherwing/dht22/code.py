# https://learn.adafruit.com/dht/dht-circuitpython-code
# https://learn.adafruit.com/adafruit-2-4-tft-touch-screen-featherwing/2-4-tft-featherwing

import time

import adafruit_dht
import board
import terminalio
import displayio
from adafruit_display_text import label
import adafruit_ili9341

dht = adafruit_dht.DHT22(board.A2)

# Release any resources currently in use for the displays
displayio.release_displays()

spi = board.SPI()
tft_cs = board.D9
tft_dc = board.D10

display_bus = displayio.FourWire(
    spi, command=tft_dc, chip_select=tft_cs, reset=board.D6
)
display = adafruit_ili9341.ILI9341(display_bus, width=320, height=240)

while True:
    try:
        temperature = dht.temperature * 9 / 5 + 32
        humidity = dht.humidity
        # Print what we got to the REPL
        print("Temp: {:.1f} *F".format(temperature))
        print("Humidity: {}%".format(humidity))
    except RuntimeError as e:
        # Reading doesn't always work! Just print error and we'll try again
        print("Reading from DHT failure: ", e.args)

    time.sleep(1)

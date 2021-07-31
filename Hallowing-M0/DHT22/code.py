# https://learn.adafruit.com/dht/dht-circuitpython-code

import time

import adafruit_dht
import board
import terminalio
from adafruit_display_text import label

dht = adafruit_dht.DHT22(board.A2)

display = board.DISPLAY
font = terminalio.FONT
color = 0x0000FF

while True:
    try:
        temperature = dht.temperature * 9 / 5 + 32
        humidity = dht.humidity
        text_temp = "Temp: {:.1f} *F".format(temperature)
        text_humid = "Humidity: {}%".format(humidity)
        # Print what we got to the REPL
        print(text_temp)
        print(text_humid)
        text_area = label.Label(font, text=text_temp, color=color)
        text_area.x = 20
        text_area.y = 20
        display.show(text_area)
    except RuntimeError as e:
        # Reading doesn't always work! Just print error and we'll try again
        print("Reading from DHT failure: ", e.args)

    time.sleep(2)

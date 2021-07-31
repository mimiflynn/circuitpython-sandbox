# https://learn.adafruit.com/dht/dht-circuitpython-code

import time

import adafruit_dht
import board


dht = adafruit_dht.DHT22(board.D6)

while True:
    try:
        temperature = dht.temperature * 9 / 5 + 32
        humidity = dht.humidity
        # Print what we got to the REPL
        print("Temp: {:.1f} *C \t Humidity: {}%".format(temperature, humidity))
    except RuntimeError as e:
        # Reading doesn't always work! Just print error and we'll try again
        print("Reading from DHT failure: ", e.args)

    time.sleep(1)

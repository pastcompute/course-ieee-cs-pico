import board
import digitalio
import time
import adafruit_dht
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
led.value = True
dht = adafruit_dht.DHT11(board.GP8)
time.sleep(3.0)
while True:
    try:
        led.value = True
        t = dht.temperature
        h = dht.humidity
        time.sleep(0.2)
        print(dht.temperature, dht.humidity)
        led.value = False
        time.sleep(0.8)
    except RuntimeError as e:
        print("DHT error", e.args)
        time.sleep(3.0)


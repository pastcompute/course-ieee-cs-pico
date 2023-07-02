import board
import digitalio
import time
import adafruit_dht
import busio
import adafruit_ssd1306
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
led.value = True
i2c = busio.I2C(board.GP21, board.GP20)
display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
display.fill(0)
display.show()
dht = adafruit_dht.DHT11(board.GP8)
time.sleep(3.0)
while True:
    try:
        led.value = True
        t = dht.temperature
        h = dht.humidity
        time.sleep(0.2)
        print(t, h)
        display.fill(0)
        display.text("{:2d}%".format(h), 4, 8, True, size=2)
        display.text("{:4.1f}".format(t), 50, 8, True, size=2)
        display.text("o".format(t), 98, 6, True, size=1)
        display.show()
        led.value = False
        time.sleep(0.8)
    except RuntimeError as e:
        print("DHT error", e.args)
        time.sleep(3.0)

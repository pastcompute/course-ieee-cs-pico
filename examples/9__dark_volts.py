import board
import digitalio
import time
import busio
import adafruit_ssd1306
import analogio

ldr = analogio.AnalogIn(board.A1)
i2c = busio.I2C(board.GP21, board.GP20)
display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
display.fill(0)
display.show()
while True:
    v = ldr.value
    volts = v * 3.3 / 65535
    print(v, volts)
    display.fill(0)
    display.text("{:.1f}V".format(volts), 4, 8, True, size=2)
    display.show()
    time.sleep(1.0)

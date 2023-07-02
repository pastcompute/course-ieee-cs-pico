import board
import digitalio
import time
import busio
import adafruit_ssd1306

i2c = busio.I2C(board.GP21, board.GP20)
display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

counter = 0
display.fill(0)
while True:
    display.show()
    time.sleep(1.0)
    display.fill(0)
    display.text("{}".format(counter), 4,8, True, size=2)
    counter = counter + 1

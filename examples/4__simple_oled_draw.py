import board
import digitalio
import time
import busio
import adafruit_ssd1306
i2c = busio.I2C(board.GP21, board.GP20)
display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
display.fill(0)
display.show()
dw = display.width
dh = display.height
display.line(1, 1, dw - 2, dh - 2, True)
display.line(dw-2, 1, 1, dh-2, True)
display.show()


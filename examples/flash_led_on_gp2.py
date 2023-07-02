import board
import digitalio
import time

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

led2 = digitalio.DigitalInOut(board.GP2)
led2.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    led2.value = False
    time.sleep(0.5)
    led.value = False
    led2.value = True
    time.sleep(0.5)


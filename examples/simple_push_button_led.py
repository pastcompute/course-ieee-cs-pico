import board
import digitalio
import time

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

button1 = digitalio.DigitalInOut(board.GP26)
button1.direction = digitalio.Direction.INPUT
led.value = False

while True:
    time.sleep(0.1)
    if button1.value == True:
        print("on")
        led.value = True
    else:
        print("off")
        led.value = False


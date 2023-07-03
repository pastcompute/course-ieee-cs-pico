import pwmio
import time
import board
import analogio

buzzer = pwmio.PWMOut(board.GP18, frequency=750, variable_frequency=True, duty_cycle=0)
ldr = analogio.AnalogIn(board.A1)

threshold = 17000
while True:
    if ldr.value < threshold:
        buzzer.frequency = 750
        buzzer.duty_cycle = int(65536 / 2)
    else:
        buzzer.duty_cycle = 0
    time.sleep(0.1)

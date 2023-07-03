import pwmio
import time
import board
import analogio

buzzer = pwmio.PWMOut(board.GP18, frequency=750, variable_frequency=True, duty_cycle=0)
ldr = analogio.AnalogIn(board.A0)

threshold = 27000
while True:
    v = ldr.value
    if v < 64000: print(v)
    if v < threshold:
        buzzer.frequency = 750
        buzzer.duty_cycle = int(65536 / 2)
        time.sleep(2)
    else:
        buzzer.duty_cycle = 0
    time.sleep(0.01)
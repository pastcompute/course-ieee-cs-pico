import pwmio
import time
import board

buzzer = pwmio.PWMOut(board.GP18, frequency=750, variable_frequency=True, duty_cycle=0)

while True:
    for i in range(10):
        buzzer.frequency = 750 + i * 40
        buzzer.duty_cycle = int(65536 / 2)
        time.sleep(0.1)

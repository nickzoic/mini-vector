from machine import Pin, DAC
from time import ticks_us

dac_x = DAC(Pin(25))
dac_y = DAC(Pin(26))

while True:
    a = ticks_us()
    dac_x.write(0)
    b = ticks_us()
    dac_y.write(0)
    c = ticks_us()
    dac_x.write(255)
    d = ticks_us()
    dac_y.write(255)
    e = ticks_us()
    print(f"{b-a} {c-b} {d-c} {e-d}")


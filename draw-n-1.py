from itertools import cycle

from machine import Pin, DAC

dac_x = DAC(Pin(25))
dac_y = DAC(Pin(26))

points = [
        (0.0, 0.0),
        (0.0, 1.0),
        (0.25, 1.0),
        (0.75, 0.5),
        (0.75, 1.0),
        (1.0, 1.0),
        (1.0, 0.0),
        (0.75, 0.0),
        (0.25, 0.5),
        (0.25, 0.0),
]

for x, y in cycle(points):
    dac_x.write(int(x*255))
    dac_y.write(int(y*255))


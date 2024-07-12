from itertools import cycle

try:
    from itertools import pairwise
except ImportError:
    def pairwise(iterable):
        it = iter(iterable)
        a = next(it)
        for b in it:
            yield a, b
            a = b

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

steps = 8

for (x1, y1), (x2, y2) in pairwise(cycle(points)):
    for s in range(0, steps):
        f = s / steps
        x = int((x1 * (1-f) + x2 * f)*255)
        y = int((y1 * (1-f) + y2 * f)*255)
        dac_x.write(x)
        dac_y.write(y)


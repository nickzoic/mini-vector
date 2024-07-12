from itertools import cycle, pairwise

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

steps = 128

for (x1, y1), (x2, y2) in pairwise(cycle(points)):
    for s in range(0, steps):
        f = s / steps
        x = x1 * (1-f) + x2 * f
        y = y1 * (1-f) + y2 * f
        print(x,y)


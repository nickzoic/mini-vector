# convert paths found in an SVG to a python
# array of arrays of point tuples.

INTERPOLATE = 2

from xml.dom import minidom
from svg.path import parse_path

import sys

# find all the paths in the SVG
doc = minidom.parse(sys.argv[1])
path_strings = [ path.getAttribute('d') for path in doc.getElementsByTagName('path') ]
doc.unlink()

print("characters = [")

for ps in path_strings:
    parsed_path = parse_path(ps)
    prev_point = None
    
    print("\t[")

    # use this to remove offset and scale paths
    x1, y1, x2, y2 = parsed_path.boundingbox()

    for segment in parsed_path:
        ll = segment.length()

        # remove very small segments
        if ll < 0.0000001: continue

        n = int(INTERPOLATE * ll + 1)
        for l in range(0, n+1):
            point = segment.point(l/n)
            if point != prev_point:
                x = (point.real - x1) / (x2 - x1)
                y = (y2 - point.imag) / (y2 - y1)
                print(f"\t\t({x:.3f}, {y:.3f}),")
                prev_point = point
    print("\t],")

print("]")

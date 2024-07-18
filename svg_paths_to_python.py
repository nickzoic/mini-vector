# convert paths found in an SVG to a python
# array of arrays of point tuples.

from xml.dom import minidom
from svg.path import parse_path

import sys
from struct import pack
from binascii import hexlify

# find all the paths in the SVG
doc = minidom.parse(sys.argv[1])
path_strings = [ path.getAttribute('d') for path in doc.getElementsByTagName('path') ]
doc.unlink()

def path_to_points(parsed_path, interpolate=2):
    # use this to remove offset and scale paths
    x1, y1, x2, y2 = parsed_path.boundingbox()
    prev_point = None

    for segment in parsed_path:
        ll = segment.length()

        # remove very small segments
        if ll < 0.0000001: continue

        n = int(interpolate * ll + 1)
        for l in range(0, n+1):
            point = segment.point(l/n)

            # remove repeated points
            if point != prev_point:
                x = (point.real - x1) / (x2 - x1)
                y = (y2 - point.imag) / (y2 - y1)
                yield x, y
                prev_point = point

print("characters = [")
for n, ps in enumerate(path_strings):
    #print('"' + hexlify(bytearray(int(n*255) for x, y in path_to_points(parse_path(ps)) for n in (x, y))).decode('ascii') + f'", # {n}')
    print(f"\t[ # {n}")
    for x, y in path_to_points(parse_path(ps)):
        print(f"\t\t({x:.3f}, {y:.3f}),")
    print("\t],")

print("]")

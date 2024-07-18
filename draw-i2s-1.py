from machine import I2S
from machine import Pin
from struct import pack

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

I2S_ID = 0
SCK_PIN = 32
WS_PIN = 25
SD_PIN = 33
BUFFER_LENGTH_IN_BYTES = 20000 
SAMPLE_RATE_IN_HZ = 22050

i2s_out = I2S(
    I2S_ID,
    sck=Pin(SCK_PIN),
    ws=Pin(WS_PIN),
    sd=Pin(SD_PIN),
    mode=I2S.TX,
    bits=16,
    format=I2S.STEREO,
    rate=SAMPLE_RATE_IN_HZ,
    ibuf=BUFFER_LENGTH_IN_BYTES,
)

buffer = pack("<" + "h" * (2*len(points)), *[int(z * 0x4000 + 0x8000) for x, y in points for z in (x,y)])
try:
    while True:
        i2s_out.write(buffer)
finally:
    i2s_out.deinit()


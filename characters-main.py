from machine import I2S
from machine import Pin
from struct import pack
from time import time
from characters import characters

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

    
while True:
    t = time()
    points = (
        [ ((x+0)/3, y) for x, y in characters[t//9%3] ] +
        [ (0.333, 0) ] +
        [ ((x+1)/3, y) for x, y in characters[t//3%3] ] +
        [ (0.666, 0) ] +
        [ ((x+2)/3, y) for x, y in characters[t%3] ] +
        [ (1, 0), (1, 0), (0.666, 0), (0.333, 0), (0, 0), (0, 0) ] 
    )
    buffer = pack("<" + "h" * (2*len(points)), *[int(z * 0xFFFF - 0x8000) for x, y in points for z in (x,y)])
    while t == time():
        i2s_out.write(buffer)


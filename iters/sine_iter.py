"""
sine_iter
"""
import math

from synth.decorators import length

@length(lambda length,f,a=0,samprate=44100: length*samprate)
def sine_iter(length,freq,amp=1,samprate=44100):
    """
    A string iterator that returns a 2-bytes representation of a sine wave,
    with given length (sec), freq (herz), amplitude [0..1], and sample rate
    (herz).
    """
    k1 = float(freq)*2*math.pi/samprate
    k2 = 0x7fff*amp
    for i in xrange(int(length*samprate)):
        yield [int(math.sin(i*k1)*k2 + 0.5)],1

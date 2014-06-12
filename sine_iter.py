"""
sine_iter
"""
import math

def sine_iter(length,freq,samprate):
    """
    A string iterator that returns a 2-bytes representation of a sine wave,
    with given length (sec), freq (herz), and sample rate (herz).
    """
    for i in xrange(int(length*samprate)):
        d = math.sin((float(i)/samprate)*freq*2*math.pi)
        x = int(d*3000)+8000
        yield chr(x&(1<<8-1)) + chr(x>>8)

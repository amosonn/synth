"""
iterators.
"""
import math
import itertools as it

from .tools import streamify

@streamify
def sine_iter(freq,amp=1,samprate=44100):
    """
    A string iterator that returns a 2-bytes representation of a sine wave,
    with given length (sec), freq (herz), amplitude [0..1], and sample rate
    (herz).
    """
    k1 = float(freq)*2*math.pi/samprate
    for i in it.count():
        yield math.sin(i*k1)*amp

"""
iterators.
"""
import itertools as it

from .tools import streamify, amp, sHz

@streamify
def sine_iter(freq,gain=1,samprate=44100):
    """
    A string iterator that returns a 2-bytes representation of a sine wave,
    with given length (sec), freq (herz), amplitude [0..1], and sample rate
    (herz).
    """
    s,h = sHz(samprate)
    for i in it.count():
        yield amp(freq,h,i)

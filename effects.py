"""
Effects which take a single bit or a stream of bits, and modify it.
"""
import itertools

from .tools import streamify, sHz

@streamify
def multi_harmonize(sb,gain_iters=None):
    """
    Returns a stream of different harmonizations of sb.

    Input:
        sb: SoundBit to harmonize.
        gain_iters: list of iterators, giving the harmonization coeffs for each
            frame.
    """
    if gain_iters is None:
        gain_iter = itertools.repeat((1.0,))
    else:
        gain_iter = itertools.izip_longest(*gain_iters,fillvalue=0.0)
    for gain_list in gain_iter:
        sb2 = sb.copy()
        sb2.harmonize(gain_list)
        yield sb2

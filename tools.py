"""
Various tools for easier work.
"""
from functools import wraps
from audiolazy import Stream, sHz
import math

def streamify(gen):
    """
    Take a generator and make it return streams.
    """
    @wraps(gen)
    def _g(*args,**kwargs):
        g = gen(*args,**kwargs)
        return Stream(g)
    return _g

@streamify
def buffer_stream(stream,length,frac):
    """
    Assuming only a given length of a given stream is wanted, buffers
    a fraction of it, and keeps reading at a lower pace from the original
    stream. Rounds frac to the nearst 1/1000, to escape floating-point
    errors.
    """
    n = int(frac*1000)
    stream.limit(length)
    to_read_1000 = length*n
    int_to_read = to_read_1000 / 1000
    rem = to_read_1000 % 1000
    buf = stream.take(int_to_read)
    op_n = 1000 - n
    while True:
        rem += op_n
        if rem >= 1000:
            try:
                val = stream.take()
            except StopIteration:
                for x in buf:
                    yield x
                break
            buf.append(val)
            rem -= 1000
        yield buf[0]
        del buf[0]

def amp(freq,h,t):
    """
    Returns the amplitude of a single point given the frequency,
    h = 2*pi / samprate, and running time in samples.
    """
    return math.sin(t*float(freq)*h)

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
        if len(buf) > 0:
            yield buf[0]
        else:
            try:
                stream.take()
            except StopIteration:
                break
            else:
                raise AssertionError("Iterator should be empty.")
        del buf[0]

@streamify
def nat_buffer_stream(stream,length,ratio):
    """
    Assuming only a given length of a given stream is wanted, buffers
    a fraction of it required to read from the stream only once every
    ratio outputs.
    """
    stream.limit(length)
    to_read = int(math.ceil(length * float(ratio-1) / ratio))
    buf = stream.take(to_read)
    for val in stream:
        buf.append(val)
        for i in xrange(ratio):
            yield buf[i]
        del buf[:ratio]
    for val in buf:
        yield val


def amp(freq,h,t):
    """
    Returns the amplitude of a single point given the frequency,
    h = 2*pi / samprate, and running time in samples.
    """
    return math.sin(t*float(freq)*h)

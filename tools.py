"""
Various tools for easier work.
"""
from functools import wraps
from audiolazy import Stream

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
    stream.
    """
    stream.limit(length)
    to_read = length*frac
    int_to_read = int(to_read)
    rem = to_read - int_to_read
    buf = stream.take(int_to_read)
    op_frac = 1 - frac
    while True:
        rem += op_frac
        if rem >= 1:
            try:
                val = stream.take()
            except StopIteration:
                for x in buf:
                    yield x
                break
            buf.append(val)
            rem -= 1
        yield buf[0]
        del buf[0]

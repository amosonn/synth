"""
num_to_str_iter
"""
from synth.decorators import length

@length(lambda iter: 2 * len(iter))
def num_to_str_iter(iter):
    """
    Takes a 16bit unsigned number iterator, and yields for each value,
    a tuple of 2bytes representation of the number (shifted by 0x8000 up).
    """
    for vals in iter:
        yield "".join([chr(x&0xff) + chr(((x>>8)&0xff)^0x80) for x in vals])

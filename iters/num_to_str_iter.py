"""
num_to_str_iter
"""
class num_to_str_iter(object):
    """
    Takes a 16bit unsigned number iterator, and yields for each value,
    a tuple of 2bytes representation of the number (shifted by 0x8000 up),
    and the length.
    """
    def __init__(self,iter):
        self._iter = iter

    def __len__(self):
        return 2 * len(self._iter)

    def __iter__(self):
        return self

    def next(self):
        x = self._iter.next()
        return (chr(x&0xff) + chr(((x>>8)&0xff)^0x80),2)

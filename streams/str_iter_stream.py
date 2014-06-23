"""
StrIterStream.
"""
from streams.base_stream import BaseStream

class StrIterStream(BaseStream):
    """
    Stream wrapper for an iterator that yields (str,length) tuples.
    """
    def __init__(self,iter):
        self._iter = iter
        self._buf = ""
        # This is an optimization.
        self._buflen = 0

    def read(self,n):
        """
        Return n bytes received, cumulatively, from the iterator.
        """
        while n > self._buflen:
            try:
                a = self._iter.next()
            except StopIteration:
                break
            s,slen = a
            self._buf += s
            self._buflen += slen
        out = self._buf[:n]
        self._buf = self._buf[n:]
        self._buflen -= n
        if self._buflen < 0:
            self._buflen = 0
        return out
    
    def close(self):
        pass

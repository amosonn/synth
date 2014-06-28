"""
StrIterStream.
"""
from synth.streams.base_stream import BaseStream

class StrIterStream(BaseStream):
    """
    Stream wrapper for an iterator that yields strings.
    """
    def __init__(self,iter):
        self._iter = iter
        self._buf = ""

    def read(self,n):
        """
        Return n bytes received, cumulatively, from the iterator.
        """
        while n > len(self._buf):
            try:
                s = self._iter.next()
            except StopIteration:
                break
            self._buf += s
        out = self._buf[:n]
        self._buf = self._buf[n:]
        return out
    
    def close(self):
        pass

"""
BufStrIterStream.
"""
from synth.streams.base_stream import BaseStream
from synth.streams.str_iter_stream import  StrIterStream

class BufStrIterStream(BaseStream):
    """
    Stream wrapper for an iterator that yields strings (or (str,length) tuples)
    and has a length.
    Buffers frac (float between 0 to 1) of the iterator upon initialization,
    and keeps reading from it at (1-frac) rate.
    """
    def __init__(self,iter,frac):
        self._readfrac = 1 - frac
        first_buflen = len(iter) * frac
        self._iter_stream = StrIterStream(iter)
        # fraction residue from each read.
        int_first_buflen = int(first_buflen)
        self._res = first_buflen - int_first_buflen
        self._buf = self._iter_stream.read(int_first_buflen)

    def read(self,n):
        """
        Return n bytes received, cumulatively, from the iterator.
        raises: BadStrIter
        """
        to_read = n*self._readfrac + self._res
        int_to_read = int(to_read)
        self._res = to_read - int_to_read
        self._buf += self._iter_stream.read(int_to_read)
        # first we read, so we don't underflow near the end.
        out = self._buf[:n]
        self._buf = self._buf[n:]
        return out
    
    def close(self):
        self._iterstream.close()

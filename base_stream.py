
class BaseStream(object):
    """
    Base Stream class.
    Supports:
        read(int) - returns up to int bytes.
        close() - closes the stream.
    """

    def read(self,n):
        raise NotImplementedError()

    def close(self):
        raise NotImplementedError()

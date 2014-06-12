
class BaseStream(object):
    """
    Base Stream class.
    Supports:
        read(int) - returns up to int bytes.
        close() - closes the stream.
    """

    def read(n):
        raise NotImplementedError()

    def close():
        raise NotImplementedError()

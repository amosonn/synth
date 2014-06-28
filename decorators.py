"""
Help decorators for creating generators.
"""
from functools import wraps

class length(object):
    """
    Sets a (value,length) generator's length, by passing its arguments to
    a helper function which calculates its length.
    """
    def __init__(self,lenf):
        self._lenf = lenf

    def __call__(self,g):
        @wraps(g,("__module__","__name__"),())
        class G(object):
            def __init__(iself,*args,**kwargs):
                iself._l = self._lenf(*args,**kwargs)
                iself._g = g(*args,**kwargs)

            def __len__(iself):
                return iself._l

            def __iter__(iself):
                return iself

            def next(iself):
                value = iself._g.next()
                iself._l -= len(value)
                return value

        return G

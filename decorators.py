"""
Help decorators for creating generators.
"""
from functools import wraps

class length(object):
    """
    Sets a (value,length) generator's length.
    """
    def __init__(self,l):
        self._l = l

    def __call__(self,g):
        @wraps(g,("__module__","__name__"),())
        class G(object):
            def __init__(iself,*args,**kwargs):
                iself._g = g(*args,**kwargs)
                iself._l = self._l

            def __len__(iself):
                return iself._l

            def __iter__(iself):
                return iself

            def next(iself):
                value,length = iself._g.next()
                iself._l -= length
                return (value,length)

        return G

def yield_len(g):
    """
    Makes a generator yield a (value,length) tuple, where value is the
    original yield value and length is len(value).
    """
    @wraps(g)
    def _g(*args,**kwargs):
        for i in g(*args,**kwargs):
            yield (i,len(i))

    return _g


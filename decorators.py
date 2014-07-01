"""
decorators.
"""
from audiolazy import Stream

def streamify(gen):
    """
    Take a generator and make it return streams.
    """
    def _g(*args,**kwargs):
        g = gen(*args,**kwargs)
        return Stream(g)
    return _g

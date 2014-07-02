"""
A single bit of sound, and some basic functions operating on them.
"""
import math

# The range of frequencies we work in is around [20,20000].
# We want to work in log scale, preferably log2 so ocatves are perfect.
# our range in log2 is [4,14]. We want to work with ints, so we scale this by
SCALE = 1000
# so now we have 10000 different freqs.

from .tools import streamify, sHz
from . import tools

class SoundBit(object):
    """
    The smallest unit of measure for sound, as implemented in this code.
    Contains frquencies and corresponding amplitudes.
    """
    def __init__(self, data_dict=None):
        """
        Init SoundBit.
        
        Input:
            data_dict: A dictionary.
        """
        if data_dict is None:
            self._data = {}
        else:
            self._data = {_lin_to_log(freq): amp for \
                (freq,amp) in data_dict.iteritems()}
    
    def __iadd__(self, other):
        """
        Add operator.
        
        Adds the amplitudes of each frequency.
        """
        if not isinstance(other, SoundBit):
            raise TypeError("SoundBit can only be added to SoundBit.")
        
        _iadd_dict(self._data,other._data)
        return self

    def __imul__(self,other):
        """
        Multiply every frequency by a constant number.
        """
        if not isinstance(other,(int,float)):
            raise TypeError("SoundBit can only be multiplied by a number.")

        for key in self._data.iterkeys():
            self._data[key] *= other
        return self

    def harmonize(self,gain_list):
        """
        Adds the harmonies of each frequency, with given gain over the base
        frequency. The 0th item in gain_list is the gain of the base value,
        the 1st is the gain of the first harmony (2*freq), and so on.
        """
        d = self._data
        self._data = {}
        for i,gain in enumerate(gain_list):
            if gain > 0:
                # coefficient of the freqs.
                if i < len(INT_COEFF_TABLE):
                    c = INT_COEFF_TABLE[i]
                else:
                    c = _lin_to_log(i+1)
                    INT_COEFF_TABLE[i] = c
                _iadd_dict(self._data,{c+lfreq: gain*amp for lfreq,amp in \
                    d.iteritems()})
    
    def get_amp(self, h, t):
        """
            Return amplitude at a given point in time.
            
            Input:
                h: 2*pi / samprate.
                t: sample index (not sec).
            Return:
                The sum of amplitudes of all sines in sound_bit at time t.
        """
        return sum([amp * tools.sine_amp(_log_to_lin(lfreq),h,t) for \
            lfreq, amp in self._data.items()])

    def __add__(self, other):
        """
        Add operator.
        
        Adds the amplitudes of each frequency.
        """
        soundbit_copy = self.copy()
        soundbit_copy += other
        return soundbit_copy

    def __mul__(self,other):
        """
        Copy and multiply every frequency by a constant number.
        """
        s = self.copy()
        s *= other
        return s

    def __rmul__(self,other):
        """
        Copy and multiply every frequency by a constant number.
        """
        return self * other

    def __eq__(self,other):
        if not isinstance(other, SoundBit):
            raise TypeError("SoundBit can only be compared to SoundBit.")
        return self._data == other._data

    def __ne__(self,other):
        return not self == other

    def __repr__(self):
        return "SoundBit: %r" % (self._data,)

    def __str__(self):
        return "SoundBit: %s" % (self._data,)
    
    def copy(self):
        sb = SoundBit()
        sb._data = self._data.copy()
        return sb

@streamify
def sb_to_amp(stream,rate=44100):
    """
    Convert a stream of sbs to a stream of [-1,1] floats.

    Input:
        stream: audiolazy.Stream(SoundBit)
        rate: samprate in Hz
    """
    s,h = sHz(rate)
    for t,sb in enumerate(stream):
        yield sb.get_amp(h,t)

def _iadd_dict(d1,d2):
    """
    Add the (key,values) in d2 to d1; if a key is present in both, the values are
    added. Is preformed in-place.
    """
    for key_other, val_other in d2.iteritems():
        d1.setdefault(key_other,0)
        d1[key_other] += val_other

def _lin_to_log(lin):
    """
    Convert from linear scale (freq in Hz) to log scale (4000 to 14000)
    """
    return int(SCALE * math.log(lin,2))

def _log_to_lin(log):
    """
    Convert from log scale (4000 to 14000) to linear scale (freq in Hz)
    """
    return 2 ** (float(log)/SCALE)

INT_COEFF_TABLE = [_lin_to_log(n) for n in xrange(1,20)]

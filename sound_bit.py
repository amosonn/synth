ZERO_VAL = 0 # self.data's zero.

class SoundBit(object):
    """
    The smallest unit of measure for sound, as implemented in this code/
    Contains frquencies and corresponding amplitudes.
    """
    def __init__(self, data_dict):
        """
        Init SoundBit.
        
        Input:
            data_dict: A dictionary.
        """
        self._data = data_dict.copy()
    
    def __iadd__(self, other):
        """
        Add operator.
        
        Adds the amplitudes of each frequency.
        """
        if not isinstance(other, SoundBit):
            raise TypeError("SoundBit can only be added to SoundBit.")
        
        iadd_dict(self._data,other._data)
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
            # coefficient of the freqs.
            c = i+1
            iadd_dict(self._data,{c*freq: gain*amp for freq,amp in \
                d.iteritems()})

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
        return self._dict == other._dict

    def __ne__(self,other):
        return not self == other
    
    def copy(self):
        return SoundBit(self._data)

def iadd_dict(d1,d2):
    """
    Add the (key,values) in d2 to d1; if a key is present in both, the values are
    added. Is preformed in-place.
    """
    for key_other, val_other in d2.iteritems():
        d1.setdefault(key_other,0)
        d1[key_other] += val_other

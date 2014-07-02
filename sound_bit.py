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
    
    def __add__(self, other):
        """
        Add operator.
        
        Adds the amplitudes of each frequency.
        """
        soundbit_copy = self.copy()
        
        soundbit_copy += other
        
        return soundbit_copy
    
    def __iadd__(self, other):
        """
        Add operator.
        
        Adds the amplitudes of each frequency.
        """
        if not isinstance(other, SoundBit):
            raise TypeError('SoundBit can only be added to SoundBit.')
        
        for (key_other, val_other) in other._data.iteritems():
            self._data.setdefault(key_other,0)
            self._data[key_other] += val_other
        
        return self
    
    def copy(self):
        return SoundBit(self._data)
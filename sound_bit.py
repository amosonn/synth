ZERO_VAL = 0 # self.data's zero.

class SoundBit(object):
    def __init__(self, data_dict):
        self._data = data_dict
    
    def get_data(self, key):
        return self._data
    
    def __add__(self, other):
        joined_data = dict()
        
        data_other = other.get_data()
        
        for (key_self, val_self) in self._data.iteritems():
            val_other = data_other.get(key, ZERO_VAL)
            joined_data[key_self] = val_self + val_other
        
        for (key_other, val_other) in data_other.iteritems():
            if key_other not in self._data:
                joined_data[key_other] = val_other
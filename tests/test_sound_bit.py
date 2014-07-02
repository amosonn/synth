from synth.sound_bit import SoundBit
from synth import tools

RATE = 44100

def test_add():
    """
    Test add.
    
    Description:
    Assert that:
    1. Dictionaries were unchanged.
    2.Original SoundBits were unchanged.
    3. Add operation was successful.
    """
    d1 = {440:0.5, 880:0.7}
    d2 = {440:0.5, 660:0.2}
    expected_result_dict = {440:1, 660:0.2, 880:0.7}
    
    # Save a copy of all dictionaries, in order to check that the dictionaries
    # remained unchanged.
    d1_backup = d1.copy()
    d2_backup = d2.copy()
    expected_result_dict_backup = expected_result_dict.copy()
    
    sb1 = SoundBit(d1)
    sb2 = SoundBit(d2)
    
    result_sb = sb1 + sb2
    
    assert d1 == d1_backup
    assert d2 == d2_backup
    assert expected_result_dict == expected_result_dict_backup
    assert sb1 == SoundBit(d1)
    assert sb2 == SoundBit(d2)
    assert result_sb == SoundBit(expected_result_dict)

def test_get_amp_single_freq():
    freq = 1
    amp = 1
    sb = SoundBit({freq:amp})
    
    s, Hz = tools.sHz(RATE)
    
    t_list = range(2*RATE)

    get_amp_results = [sb.get_amp(Hz, t) for t in t_list]
    direct_compute_results = [tools.sine_amp(freq, Hz, t) for t in t_list]
    
    assert get_amp_results == direct_compute_results
    
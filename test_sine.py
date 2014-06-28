import time

from synth.out.player import Player
from synth.iters.sine_iter import sine_iter
from synth.iters.num_to_str_iter import num_to_str_iter
from synth.streams.str_iter_stream import StrIterStream

def test_sine():
    p = Player()
    si = sine_iter(2,440,amp=0.3)
    sis = StrIterStream(num_to_str_iter(si))
    p.play(sis)
    time.sleep(2)

    #assert raw_input("Did you hear a sound? [N/y]") in "yY"

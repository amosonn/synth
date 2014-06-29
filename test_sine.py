import time

from synth.out.player import Player
from synth.iters.sine_iter import sine_iter
from synth.iters.num_to_str_iter import num_to_str_iter
from synth.iters.coeff_sum_iter import coeff_sum_iter
from synth.streams.str_iter_stream import StrIterStream

def test_sine():
    p = Player()
    si = sine_iter(2,440,amp=0.3)
    sis = StrIterStream(num_to_str_iter(si))
    p.play(sis)
    time.sleep(2)

    #assert raw_input("Did you hear a sound? [N/y]") in "yY"

def test_two_sines():
    p = Player()
    si440 = sine_iter(2,440)
    si660 = sine_iter(2,660)
    sis = StrIterStream(num_to_str_iter(coeff_sum_iter( \
        (0.5,si440),(0.5,si660))))
    p.play(sis)
    time.sleep(2)

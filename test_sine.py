import os

from synth.out.player import Player
from synth.out.wav_write import wav_write
from synth.iters.sine_iter import sine_iter
from synth.iters.num_to_str_iter import num_to_str_iter
from synth.iters.coeff_sum_iter import coeff_sum_iter
from synth.streams.str_iter_stream import StrIterStream
from synth.streams.buf_str_iter_stream import BufStrIterStream

def test_sine():
    p = Player()
    si = sine_iter(2,440,amp=0.3)
    sis = StrIterStream(num_to_str_iter(si))
    p.play(sis)
    p.wait()
    p.close()

    #assert raw_input("Did you hear a sound? [N/y]") in "yY"

def test_two_sines_buffered(tmpdir):
    p = Player()
    si440 = sine_iter(2,440)
    si660 = sine_iter(2,660)
    bsis = BufStrIterStream(num_to_str_iter(coeff_sum_iter( \
        (0.5,si440),(0.5,si660))),0.5)
    bsis.read(100)
    p.play(bsis)
    p.wait()
    p.close()

def not_test_two_sines_wav(tmpdir):
    #p = Player()
    si440 = sine_iter(2,440)
    si660 = sine_iter(2,660)
    sis = StrIterStream(num_to_str_iter(coeff_sum_iter( \
        (0.5,si440),(0.5,si660))))
    fname = str(tmpdir.join("a.wav"))
    wav_write(fname,sis)
    os.system("aplay %s" % fname)
    #p.play(sis)
    #p.wait()
    #p.close()


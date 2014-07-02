import os

from synth.iters import sine_iter
from synth.out import play

def test_play():
    si = sine_iter(440,gain=0.3)
    play(si,2)

def test_buffered_play():
    si = sine_iter(440,gain=0.3)
    play(si,2,ratio=5)

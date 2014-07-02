"""
wav_write.
"""
import wave
from audiolazy import AudioIO
from .tools import nat_buffer_stream

def wav_write(fname,stream,rate=44100,width=2,channels=1):
    """
    Write to a file named fname the data in stream, with given params.
    """
    w = wave.open(fname,"w")
    w.setframerate(rate)
    w.setsampwidth(width)
    w.setnchannels(channels)
    while True:
        a = stream.read(1024)
        if len(a) == 0:
            break
        else:
            w.writeframes(a)
    stream.close()
    w.close()

def play(stream,duration,ratio=-1,rate=44100):
    with AudioIO(True) as player:
        if ratio != -1:
            player.play(nat_buffer_stream(stream,int(rate*duration),ratio), \
                rate=rate) 
        else:
            player.play(stream.take(int(rate*duration)),rate=rate) 

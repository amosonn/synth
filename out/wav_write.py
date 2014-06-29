"""
wav_write.
"""
import wave

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

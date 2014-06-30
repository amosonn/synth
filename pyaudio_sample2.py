import pyaudio
import time
#import sys
#import StringIO
import math

#if len(sys.argv) < 3:
    #print("Plays a raw file.\n\nUsage: %s filename.wav framerate" % sys.argv[0])
    #sys.exit(-1)

#f = file(sys.argv[1], 'rb')
#s = f.read()
#f.close()
#sio = StringIO.StringIO(s)
#fr = int(sys.argv[2])
fr = 44100

# instantiate PyAudio (1)
p = pyaudio.PyAudio()

def sine(length,freq,amp=1,samprate=44100):
    k1 = float(freq)*2*math.pi/samprate
    k2 = 0x7fff*amp
    for i in xrange(int(length*samprate)):
        #yield int(math.sin(i*k1)*k2 + 0.5)
        yield (float(i)/samprate) * 0x3fff - 0x8000

sine440 = sine(2,440,amp=0.0)
sine660 = sine(2,660,amp=0.0)


# define callback (2)
def callback(in_data, frame_count, time_info, status):
    #data = sio.read(2*frame_count)
    sign = pyaudio.paContinue
    a = [0] * frame_count
    for i in xrange(frame_count):
        try:
            a[i] = int(0.5 * sine440.next() + 0.5 * sine660.next())
        except StopIteration:
            sign = pyaudio.paComplete
            break
    #b = "".join([chr(x&0xff) + chr(((x>>8)&0xff)^0x80) for x in a])
    b = "\0\0\xff\xff" * (frame_count / 2)
    return (b, sign)

# open stream using callback (3)
stream = p.open(format=pyaudio.paInt16,
                channels=1,
                rate=fr,
                output=True,
                stream_callback=callback)

# start the stream (4)
stream.start_stream()

# wait for stream to finish (5)
while stream.is_active():
    time.sleep(0.1)

# stop stream (6)
stream.stop_stream()
stream.close()

# close PyAudio (7)
p.terminate()


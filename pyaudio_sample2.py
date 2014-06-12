import pyaudio
import time
import sys
import StringIO

if len(sys.argv) < 3:
    print("Plays a raw file.\n\nUsage: %s filename.wav framerate" % sys.argv[0])
    sys.exit(-1)

f = file(sys.argv[1], 'rb')
s = f.read()
f.close()
sio = StringIO.StringIO(s)
fr = int(sys.argv[2])

# instantiate PyAudio (1)
p = pyaudio.PyAudio()

# define callback (2)
def callback(in_data, frame_count, time_info, status):
    print(in_data, frame_count, time_info, status) 
    data = sio.read(2*frame_count)
    return (data, pyaudio.paContinue)

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


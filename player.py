"""
Class for playing byte-streams to audio.
"""
import pyaudio
import time

class Player(object):
    """
    Wrapper around the pyaudio handler.
    """
    def __init__(self):
        self._p = pyaudio.PyAudio()
        self._stream = None

    def play(self,stream,rate=44100,width=2,channels=1):
        """
        Play a Stream object (see base_stream).
        raises: StreamPlayingError
        """
        if self._stream is not None:
            if self._stream.is_active():
                raise StreamPlayingError()
            else:
                self._stream.stop_stream()
                self._stream.close()
                self._stream = None
        def callback(in_data, frame_count, time_info, status):
            data = stream.read(width*frame_count)
            return (data, pyaudio.paContinue)

        fmt = self._p.get_format_from_width(width)
        self._stream = self._p.open(format=fmt,
                        channels=channels,
                        rate=rate,
                        output=True,
                        stream_callback=callback)

        #self._stream.start_stream()

    def wait(self):
        while self._stream.is_active():
            time.sleep(0.1)
        self._stream.stop_stream()
        self._stream.close()
        self._stream = None

    def close(self):
        self._p.terminate()


class StreamPlayingError(Exception):
    pass

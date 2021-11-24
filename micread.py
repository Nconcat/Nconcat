import numpy as np
import pyaudio
import time
import librosa
import songify2 as sf2
import ledPat as lc

class AudioHandler(object):

    def __init__(self):
        self.FORMAT = pyaudio.paFloat32
        self.CHANNELS = 1
        self.RATE = 44100
        self.CHUNK = 1024 * 2
        self.p = None
        self.stream = None
        self.f=0

    def start(self):
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=self.FORMAT,
                                  channels=self.CHANNELS,
                                  rate=self.RATE,
                                  input=True,
                                  input_device_index=1,# 2 ist soundcard 1 ist mic?
                                  output=False,
                                  stream_callback=self.callback,
                                  frames_per_buffer=self.CHUNK)

    def stop(self):
        self.stream.close()
        self.p.terminate()
    #def fcount()


    def callback(self, in_data, frame_count, time_info, flag):
        numpy_array = np.frombuffer(in_data, dtype=np.float32)
        #librosa.feature.mfcc(numpy_array)# war eine Testfunktion vom Beispielcode
        ft1=sf2.extractShortFt(numpy_array)
        s1=sf2.createVisArray(ft1,22050)
        self.f+=1
        if (self.f==2):
            #print("---")
            #print(s1[0])
            lc.visCom(s1[0])
            self.f=0
        return None, pyaudio.paContinue

    def mainloop(self):
        while (self.stream.is_active()): # if using button you can set self.stream to 0 (self.stream = 0), otherwise you can use a stop condition
           time.sleep(0)



audio = AudioHandler()
audio.start()     # open the the stream
audio.mainloop()  # main operations with librosa
audio.stop()

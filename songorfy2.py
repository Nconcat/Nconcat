import numpy as np
import math
import sys
import librosa
import time
import os
import simpleaudio as sa
#import pyaudio
import wave
import matplotlib.pyplot as plt
import librosa.display


name = 'sample.wav'


def plt_spectrogram(Y,sr,hop_length,y_axis="log"):
    plt.figure(figsize=(22,5))
    librosa.display.specshow(Y,sr=sr,hop_length=hop_length,
    x_axis="time",
    y_axis=y_axis)
    plt.colorbar(format="%+2.f")
    plt.show()


def extractShortFt(song):#extrahiert von einem sample die STFT und sample rate
    sample, sr=librosa.load(song,sr=None)
    Fr_Size=1024
    Hop_Size=512
    m_Scale=librosa.stft(sample,n_fft=Fr_Size,hop_length=Hop_Size)
   # print (type(m_Scale[0][0]))
   #Array , erster Wert, Hop

    print (m_Scale.shape[0])
    abs_Scale= np.abs(m_Scale)**2
    db_Scale=librosa.power_to_db(abs_Scale)
    plt_spectrogram(db_Scale,sr,Hop_Size,y_axis="log")
    print(type(db_Scale[0][0]))
    for x in range(abs_Scale.shape[0]):#------------> muss noch log visualisierung rausfinden... 64,128,256 die Frequenzen werden durch die Wahrnehmung anders aufgenommen und deshalb auch anders visualisiert
        print(str(int(db_Scale[x][300]))+" "+ str(int(22050/abs_Scale.shape[0]*x)) +" Hz to " +  str(int(22050/abs_Scale.shape[0]*(x+1)))+" Hz")#math.log(x+1)* Teilt das Array einfach in Hz Teilräume ein
# versuch mit 3^x start bei 3^4 die Stft einzuordnen
#Intervalle 0-81-243-729-2187-6561-22050 3^x// oder andere Intervalle 2^x wenn das nicht funktioniert.
#nächste funktion berechnet den Durchschnitt der Db Werte der Intervalle 3^x-3^x+1-3^x+2...
#für den Visualiser die er dann als Lichtmuster ausgibt...
    return (db_Scale)

def createVisArray(db_Array):
    
    print(db_Array.shape[0])
    visArr=np.arange(0,7,dtype=float)
    countAv=0#gibt die Anzahl der Werte an, die später zum berechnen der Durchscnitts genutzt wird.
    curAverage=0 # gibt den aufsummierten Db Wert des aktuellen Hz Intervall an. Es gibt 6 Intervalle wie oben beschrieben der Durchscnitt wird berechnet, wenn sich das Intervall ändert
    frequBin=0#gibt an in welchem frequ bin wir uns befinden 0-5 in dem Fall
    for x in range(db_Array.shape[0]):
        curAverage += db_Array[x][0]
        countAv+=1
        if(int(21050/db_Array.shape[0])*x>=3**4+frequBin):
            visArr[frequBin]=curAverage/countAv
            frequBin+=1
            curAverage=0
            countAv=0






ft1=extractShortFt(name)
createVisArray(ft1)

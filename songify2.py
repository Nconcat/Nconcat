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


#name = 'sample.wav'# weg für mic read, später wichtig?


def plt_spectrogram(Y,sr,hop_length,y_axis="log"):
    plt.figure(figsize=(22,5))
    librosa.display.specshow(Y,sr=sr,hop_length=hop_length,
    x_axis="time",
    y_axis=y_axis)
    plt.colorbar(format="%+2.f")
    plt.show()


def extractShortFt(song):#extrahiert von einem sample die STFT und sample rate
    #sample, sr=librosa.load(song,sr=44100)#später wichtig?
    sr=44100
    #print(sr)
    Fr_Size=2048
    Hop_Size=1024
    m_Scale=librosa.stft(song,n_fft=Fr_Size,hop_length=Hop_Size)
    # print (type(m_Scale[0][0]))
    #Array , erster Wert, Hop

    #print (m_Scale.shape[0])
    abs_Scale= np.abs(m_Scale)**2
    db_Scale=librosa.power_to_db(abs_Scale)
   # plt_spectrogram(db_Scale,sr,Hop_Size,y_axis="log")
    '''--------------------Visualisierung von den Hz bereichen nicht wichtig für Berechnung
    print(type(db_Scale[0][0]))
    for x in range(abs_Scale.shape[0]):#------------> muss noch log visualisierung rausfinden... 64,128,256 die Frequenzen werden durch die Wahrnehmung anders aufgenommen und deshalb auch anders visualisiert
        print(str(int(db_Scale[x][300]))+" "+ str(int(sr/abs_Scale.shape[0]*x)) +" Hz to " +  str(int(sr/abs_Scale.shape[0]*(x+1)))+" Hz")#math.log(x+1)* Teilt das Array einfach in Hz Teilräume ein
    '''
# versuch mit 3^x start bei 3^4 die Stft einzuordnen
#Intervalle 0-81-243-729-2187-6561-22050 3^x// oder andere Intervalle 2^x wenn das nicht funktioniert.
#nächste funktion berechnet den Durchschnitt der Db Werte der Intervalle 3^x-3^x+1-3^x+2...
#für den Visualiser die er dann als Lichtmuster ausgibt...
    return (db_Scale)

def createVisArray(db_Array,sl):#sr=samplerate noch einfügen
    #print(db_Array.shape[1])
    #print(db_Array.shape[0])
    visArr=np.zeros((db_Array.shape[1],6))
    countAv=0#gibt die Anzahl der Werte an, die später zum berechnen der Durchscnitts genutzt wird.
    curAverage=0 # gibt den aufsummierten Db Wert des aktuellen Hz Intervall an. Es gibt 6 Intervalle wie oben beschrieben der Durchscnitt wird berechnet, wenn sich das Intervall ändert
    frequBin=0#gibt an in welchem frequ bin wir uns befinden 0-5 in dem Fall
    curmax=0
    for y in range(1):#db_Array.shape[1]): #Anzahl der Zeitframes
       # print(visArr[y-1])
        curmax=0
        frequBin=0
        curAverage=0#---------------Db values müssen noch mit log geaveraged werden
        countAv=0
        #print("---")
        for x in range(db_Array.shape[0]):
            if(curmax<db_Array[x][y]):
                curmax=db_Array[x][y]
            curAverage += db_Array[x][y]
            countAv+=1
            if(int((sl/db_Array.shape[0]))*x>=3.04**(4+frequBin)or x==db_Array.shape[0]-1 ):#22050 oder 11000
                visArr[y][frequBin]=curmax-((curAverage/countAv)/10) # speichert den Average des Frequenzintervalls bei Zeitframe y müssten eigentlich noch geaveraged werden, aber kb drauf das mit log alles zu averagen,(zu viel Rechenarbeit, schafft der raspberry pi eh nicht in Echtzeit also dirty methode, einfach hohe Werte stärker bewerten)
                #print(curmax-((curAverage/countAv)/10))# überführt den Hz betrag in das Array
                frequBin+=1
                curAverage=0
                countAv=0
                curmax=0
        #print(visArr[y])
    return(visArr)







#ft1=extractShortFt(name)
#song="sample.wav"
#wf = wave.open(song, 'rb')
#print(wf.getframerate())
#createVisArray(ft1,int(wf.getframerate()/2))

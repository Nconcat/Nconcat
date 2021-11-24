import numpy as np

#e=np.zeros((6,6))
e=np.empty((10,6), dtype='object')
r=np.array([24,2,5,6,3,45])
print(r)
def visCom(visArr):
    f=" "
    c="+"
    word=""
    for x in range(10): #array hat 42 Zeilen 6 Spalten

        for y in range(6):
            if(int(visArr[y]/4)>10-x):
                word+=c
            else:
                word+=f
            e[x][y]=word
            word=""

    print(e)
visCom(r)

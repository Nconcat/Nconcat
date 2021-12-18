import numpy as np
import random
# Feld 20x20
import time
field=np.empty((10,10), dtype='object')
#e=np.empty((10,6), dtype='object')
for y in range(field.shape[0]):
        for k in range( field.shape[1]):
            field[y][k]=''
r=int(random.random()*100)
print (r)
location=(int(r/10),int(r%10))

field[location]="A"
snakeHeadDirection=3# 0,1,2,3... 0 up 1 left 2 right 3 down

#print (field)
#snake=(())
snakeLeng=3 #base length
#snake starts always on the top left
snakePositions=np.zeros(3)#0 is tail, 0+length is head
snakePositions2=np.zeros(4)
snakePositions[0]=0
snakePositions[1]=10
snakePositions[2]=20
for x in range(snakePositions.size):
    loc=(int(snakePositions[x]/10),int(snakePositions[x]%10))
    field[loc]=2
print (field)

###
def updateField():
    print(f) #updates the field with the snew snake positions
def snakeMove(direction):
    #.------------------------To do List
    #needs fail state exception to fail the snake when it reachs out of bounds or into himself
    #a function that knows when the sanke hit the apple and grows 1 field
    #a fucntion that prevents from moving in the opposite direction it is travelling
    if(direction==0):#move up
        field[int(snakePositions[0]/10),int(snakePositions[0]%10)]=''# snake moved 1 field so last pos snake was on is now 0
        for x in range(snakeLeng-1):
            snakePositions[x]=snakePositions[x+1]#the snake moves over it's own previous path where it was before, so if the snake moves it will move where the part infornt was moving before.
            #only the head get's a new snakePosition
        snakePositions[snakeLeng-1]=snakePositions[snakeLeng-1]-10
        field[int(snakePositions[snakeLeng-1]/10),int(snakePositions[snakeLeng-1]%10)]=2
    print (field)
    time.sleep(0.5)
    #----------------------------------------
    if(direction==1):#move up
        field[int(snakePositions[0]/10),int(snakePositions[0]%10)]=''# snake moved 1 field so last pos snake was on is now 0
        for x in range(snakeLeng-1):
            snakePositions[x]=snakePositions[x+1]#the snake moves over it's own previous path where it was before, so if the snake moves it will move where the part infornt was moving before.
            #only the head get's a new snakePosition
        snakePositions[snakeLeng-1]=snakePositions[snakeLeng-1]-1
        field[int(snakePositions[snakeLeng-1]/10),int(snakePositions[snakeLeng-1]%10)]=2
    print (field)
    time.sleep(0.5)
    #-------------------------------------
    if(direction==2):#move up
        field[int(snakePositions[0]/10),int(snakePositions[0]%10)]=''
        for x in range(snakeLeng-1):
            snakePositions[x]=snakePositions[x+1]
        snakePositions[snakeLeng-1]=snakePositions[snakeLeng-1]+1
        field[int(snakePositions[snakeLeng-1]/10),int(snakePositions[snakeLeng-1]%10)]=2
    print (field)
    time.sleep(0.5)
    #--------------------------------------------
    if (direction==3):
        field[int(snakePositions[0]/10),int(snakePositions[0]%10)]=""
        for x in range(snakeLeng-1):
            snakePositions[x]=snakePositions[x+1]
        snakePositions[snakeLeng-1]=snakePositions[snakeLeng-1]+10
        field[int(snakePositions[snakeLeng-1]/10),int(snakePositions[snakeLeng-1]%10)]=2
    print (field)
    time.sleep(0.5)
snakeMove(3)
snakeMove(3)
snakeMove(2)
snakeMove(3)
snakeMove(1)




'''value = input("Please enter a string:\n")

print(f'You entered {value}')'''

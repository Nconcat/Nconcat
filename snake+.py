import numpy as np
import random
# Feld 20x20
import time

#e=np.empty((10,6), dtype='object')



def buildSnake(field):
    snakeHeadDirection=3# 0,1,2,3... 0 up 1 left 2 right 3 down
    snakeLeng=3 #base length
#snake starts always on the top left
    snakePositions=np.zeros(3)#0 is tail, 0+length is head
    snakePositions[0]=0
    snakePositions[1]=10
    snakePositions[2]=20

    return(snakePositions,snakeLeng,snakeHeadDirection)


def buildField():
    field=np.empty((10,10), dtype='object')
    for y in range(field.shape[0]):
            for k in range( field.shape[1]):
                field[y][k]=''
    r=int(random.random()*100)
    while(r==0 or r==10or r==20):
        r=int(random.random()*100)
    location=(int(r/10),int(r%10))
    #location=((60))#test locaion to test grow
    apple=location
    apple=((5,0))
    field[apple]="A"
    return(field,apple)


def updateField(field,snake,delete,tail):

    for x in range(snake[1]):
        field[0][int(snake[0][x]/10),int(snake[0][x])%10]=2
    if (delete):
        field[0][int(tail/10),int(tail)%10]=""
    setField(field)
    print(field[0]) #updates the field with the snew snake positions

    #.------------------------To do List
    #needs fail state exception to fail the snake when it reachs out of bounds or into himself
    #a function that knows when the sanke hit the apple and grows 1 field
    #a fucntion that prevents from moving in the opposite direction it is travelling
def snakeGrow(snake,tailPos):
    r=int(random.random()*100)
    snakePositions2=np.zeros(snake[1])
    snake[1]=snake[1]+1
    snakePositions2[0]=tailPos
    for x in range(snake[1]-2):
        snakePositions2[x+1]=snake[0][x+1]





def snakeMove(field,snake,direction):#change to snake later):
    snakePositions=snake[0]
    tailPos=snakePositions[0]
    if(direction==0):#move up
        # snake moved 1 field so last pos snake was on is now 0
        for x in range(snake[1]):
            snakePositions[x]=snakePositions[x+1]#the snake moves over it's own previous path where it was before, so if the snake moves it will move where the part infornt was moving before.
            #only the head get's a new snakePosition
        snakePositions[snake[1]]=snakePositions[snake[1]]-10
        pos=int(snakePositions[snake[1]]/10),int(snakePositions[snake[1]]%10)
        if(apple==pos):
            snakeGrow(snakePositions,field,tailPos)
            updateField(field,snakePositions)
        print (field)
    time.sleep(0.5)
    #----------------------------------------
    if(direction==1):#move up
        for x in range(snake[1]):
            snakePositions[x]=snakePositions[x+1]#the snake moves over it's own previous path where it was before, so if the snake moves it will move where the part infornt was moving before.
            #only the head get's a new snakePosition
        snakePositions[snake[1]]=snakePositions[snake[1]]-1
        pos=int(snakePositions[snake[1]]/10),int(snakePositions[snake[1]]%10)
        if(apple==pos):
            snakeGrow()
            updateField(field,snakePositions)
        print (field)
    time.sleep(0.5)
    #-------------------------------------
    if(direction==2):#move up
        for x in range(snake[1]):
            snakePositions[x]=snakePositions[x+1]
        snakePositions[snake[1]]=snakePositions[snake[1]]+1
        pos=int(snakePositions[snake[1]]/10),int(snakePositions[snake[1]]%10)
        if(apple==pos):
            snakeGrow()
            updateField()
        print (field)
    time.sleep(0.5)
    #--------------------------------------------
    if (direction==3):
        for x in range(snake[1]-1):
            snakePositions[x]=snakePositions[x+1]
        snakePositions[snake[1]-1]=snakePositions[snake[1]-1]+10
        pos=int(snakePositions[snake[1]-1]/10),int(snakePositions[snake[1]-1]%10)
        snake=snakePositions,snake[1]
        updateField(field,snake,True,tailPos)
        if(field[1]==pos):
            snakeGrow()
            updateField()
        #print (field[0])
    time.sleep(0.3)

def setField(ff):
    f1=ff
def setSnake(sn):
    s1=sn

f1=buildField()#0 is field 1 is apple
s1=buildSnake(f1[0])#snake multiple objects 0 is pos 1 is len 2 is direction of head
snakeMove(f1,s1,3)
snakeMove(f1,s1,3)
snakeMove(f1,s1,3)#print(f1[1])



'''value = input("Please enter a string:\n")

print(f'You entered {value}')'''

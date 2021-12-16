import numpy as np
import random
# Feld 20x20
field=np.zeros((10,10))

r=int(random.random()*100)
print (r)
location=(int(r/10),int(r%10))

field[location]=4
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

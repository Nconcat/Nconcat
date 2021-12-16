import numpy as np
import msvcrt
import time

#value = input("Please enter a string:\n")

#print(f'You entered {value}')


def kbfunc():
   x = msvcrt.kbhit()
   if x:
      ret = ord(msvcrt.getch())
   else:
      ret = 0
   return ret

while (True):
    time.sleep(0.1)
    print(kbfunc())

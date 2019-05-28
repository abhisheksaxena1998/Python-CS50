from cs50 import get_int
from sys import argv

h=get_int("Height : ")
if h<1 or h>8:
    h=get_int("Height : ")
i=h
while (i>0):
        x=1
        while (x<i):
            print(" ",end="")
            x+=1
        y=i
        while (y<=h):
            print("#",end="")
            y+=1
        print()
        i-=1
'''4. Calculate the area of the triangle using side value. [note use sqrt function to calculate the square root [ Syntax is sqrt(value)]'''
from math import sqrt
a,b,c = float(input('enter side a')),float(input('enter side b')),float(input('enter side c'))
s=float((a+b+c))
print("the area is ",sqrt((s-a)*(s-b)*(s-c)))

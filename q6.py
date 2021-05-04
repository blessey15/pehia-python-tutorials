(c, h) = (50, 30)
import math
def sqroot(d):
    q = (2*c*d)/h
    return q

l=[]
print('Enter the values of d:')
x = list(map(int , input().split(',')))
for i in x:
    y=sqroot(i)
    print(int(math.sqrt(y)), end=',')


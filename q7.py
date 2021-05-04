l=[]
print('Enter the no. of rows & columns:')
(r, c)=map(int, input().split(','))
for i in range(r):
    a=[]
    for j in range(c):
        y=i*j
        a.append(y)
    l.append(a)
print(l)

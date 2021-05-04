print('Enter the words:')
x = list(input().split(','))
x.sort()
for y in x:
    print(y, end=',')

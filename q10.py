x = list(input().split(' '))
y = []
for i in x:
    if i not in y:
        y.append(i)

for j in y:
    print(j, end=' ')



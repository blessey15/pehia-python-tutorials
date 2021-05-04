
l = []
while True:
    line = input()
    if not line:
        break
    else:
        l.append(tuple(line.split(',')))
print(sorted(l))

# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check
# whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated
# sequence.

def decimal(n):
    return int(n, 2)


x = list(input().split(','))
for y in x:
    z = decimal(y)
    if z % 5 == 0:
        print(y)

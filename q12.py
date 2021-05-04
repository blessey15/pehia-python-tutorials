# Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the
# number is an even number. The numbers obtained should be printed in a comma-separated sequence on a single line.


for i in range(1000, 3001):
    s = str(i)
    f = 0
    for j in s:
        if int(j) % 2 != 0:
            f = 1
            break
    if f == 0:
        print(i, end=',')

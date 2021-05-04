# Use a list comprehension to square each odd number in a list.
# The list is input by a sequence of comma-separated numbers.

m = list(map(int, input().split(',')))
for i in m:
    if i % 2 != 0:
        print(i ** 2, end=',')

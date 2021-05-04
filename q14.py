# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

m = input()
(l, u) = (0, 0)
for i in m:
    if i.isupper():
        u = u+1
    if i.islower():
        l = l+1
print('UPPER CASE {0}'.format(u))
print('LOWER CASE {0}'.format(l))

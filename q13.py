# Write a program that accepts a sentence and calculate the number of letters and digits.
m = input()
(l, s) = (0, 0)
for i in m:
    if i.isalpha():
        l = l+1
    if i.isdigit():
        s = s+1
print('LETTERS {0}'.format(l))
print('DIGITS {0}'.format(s))

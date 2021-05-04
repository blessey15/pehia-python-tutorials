# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.

a = int(input())
# aa = 11 * a ; aaa = 111 * a ; aaaa = 1111 * a
res = (1111 * a) + (111 * a) + (11 * a) + a
print(res)
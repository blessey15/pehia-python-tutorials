# Write a program that computes the net amount of a bank account based a transaction log from console input. The
# transaction log format is shown as following: D 100 W 200
#
# D means deposit while W means withdrawal.

amount = 0
while True:
    l = input()
    if l:
        t, a = l.split()
        amt =int(a)
        if t == 'W' and amt > amount:
            continue
        elif t == 'D':
            amount = amount + amt
        else:
            amount = amount - amt
    else:
        break
print(amount)
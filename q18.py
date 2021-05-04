def passcheck(pwd):
    f = True
    if len(pwd) < 6:
        f = False
    if len(pwd) > 20:
        f = False
    if not any(c.isdigit() for c in pwd):
        f = False
    if not any(c.isupper() for c in pwd):
        f = False
    if not any(c.islower() for c in pwd):
        f = False
    if not any(c in ['$', '#', '@'] for c in pwd):
        f = False
    return f


passwords = list(input().split(','))
for pwd in passwords:
    p = passcheck(pwd)
    if p:
        print(pwd )

# New Time
def newtime(h, m, ht, mt):
    num = 0
    if ht >= h:
        num += (ht-h)
    else:
        num += (24+ht-h)
    if mt >= m:
        num += (mt-m)
    else:
        num -= 1
        if num < 0:
            num += 24
        num += (60 + mt - m)
    return num

h, m = map(int, input().split(':'))
ht, mt = map(int, input().split(':'))
print(newtime(h, m, ht, mt))
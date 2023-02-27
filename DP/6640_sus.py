# Suspicious Stocks
def stock(d,m,l):
    gae = [False]*(d+1)
    minm = [0] * (d + 1)
    minm[0] = m
    maxm = [0] * (d + 1)
    for i in range(1, d+1):
        if minm[i-1] >= l[i-1]:
            gae[i] = True
            minm[i] = l[i-1]
            maxm[i] = 0
        else:
            minm[i] = minm[i-1]
            gae[i] = gae[i-1]
        if gae[i-1] != False:
            maxm[i] = max(l[i-1], maxm[i-1])
            gae[i] = True
    return

def stock2(d, m, l):
    minm = [0]*(d+1)
    maxm = [0]*(d+1)
    minm[0] = m
    for i in range(1, d+1):
        if minm[i-1] <= l[i-1]:
            minm[i] = l[i-1]

    if minm[d] !=0:
        return (m//minm[d])*maxm[d] +m%minm[d]
    else:
        return 0

while True:
    d = input()
    if d == '0':
        break
    d, m = map(int, d.split())
    l = list(map(int, input().split()))
    out = stock(d,m,l)
    if out <= 0:
        print(0)
    else:
        print(out)
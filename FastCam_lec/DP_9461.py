# 파도반 수열
def pado(n):
    if n < 4:
        return 1
    d = [0]*(n+1)
    d[1], d[2], d[3] = 1, 1, 1
    for i in range(4, n+1):
        d[i] = d[i-2]+d[i-3]
    return d[-1]

t = int(input())
for _ in range(t):
    n = int(input())
    print(pado(n))
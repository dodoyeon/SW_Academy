# 피로도
def piro(a,b,c,m):
    p = 0
    work = 0
    if a > m:
        return 0
    for _ in range(24):
        p += a
        if p > m:
            p -= a
            p -= c
            if p < 0:
                p = 0
        else:
            work += b
    return work
a, b, c, m = map(int, input().split())
print(piro(a,b,c,m))
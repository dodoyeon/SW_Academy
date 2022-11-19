# 관중석
from math import gcd
def gcd_use(d1, d2):
    visited = [[False]*d2 for _ in range(d2)]
    num = 0
    for i in range(d1, d2+1):
        for j in range(1, i):
            g = gcd(i, j)
            mom, son = i//g, j//g
            if visited[mom-1][son-1] == False:
                visited[mom-1][son-1] = True
                num += 1
    return num+1

d1, d2 = map(int, input().split())
print(gcd_use(d1, d2))
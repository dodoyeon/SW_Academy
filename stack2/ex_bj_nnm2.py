# 백준 15650
n,m = map(int, input().split())
l = [(i+1) for i in range(n)]
result=[0]*m

def combination(l, n, m, level, idx):
    if level == m:
        print(' '.join(str(i) for i in result))
        return
    for i in range(idx, n):
        result[level] = l[i]
        combination(l,n,m,level+1,i+1)

# combination(l, n, m, 0, 0)

import itertools
for i in itertools.combinations(l,m):
    print(' '.join(str(j) for j in i))
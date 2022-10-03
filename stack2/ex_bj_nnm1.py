# 백준 15649
n, m = map(int, input().split())
l = [(i+1) for i in range(n)]

result = [0]*m
checked = [False]*len(l)

def permutation(l, m, level):
    if level == m:
        print(' '.join(str(i) for i in result))
        return
    for i in range(len(l)):
        if checked[i] == False:
            checked[i] = True
            result[level] = l[i]
            permutation(l, m, level+1)
            checked[i] = False

# permutation(l, m, 0)

import itertools
n, m = map(int, input().split())
l = [(i+1) for i in range(n)]
for l in itertools.permutations(l, m):
    print(' '.join(str(i) for i in l))
# 순서있음
def perm_recur(level, result, visited):
    global l, n, m
    if level == m:
        return result
    for i in range(n):
        if visited[i] ==False:
            visited[i] = True
            result[level] = l[i]
            perm_recur(level+1, result, visited)
            visited[i] = False

def permutation(l, m): # 순서 있음
    n = len(l)
    result = [0]*m
    visited = [False]*n
    perm_recur(0, result, visited)

# 순서 없음
def comb_recur(level, idx, result):
    global l, n, m
    if level == m:
        return result
    for i in range(idx, n):
        result[level] = l[i]
        comb_recur(level+1, idx+1, result)

def combination(l, m):
    result = [0]*m
    n = len(l)
    comb_recur(0, 0, result)
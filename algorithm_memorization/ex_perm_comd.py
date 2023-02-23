n = 4
m = 3
l = [1, 2, 3, 4]

n = 4
m = 3
l = [1, 2, 3, 4]

# permutation 순서있음
def perm(level, result, visited):
    global l, n, m
    if level == m:
        print(' '.join(str(i) for i in result))
        return
    for i in range(n):
        if visited[i] == False:
            visited[i] = True
            result[level] = l[i]
            perm(level + 1, result, visited)
            visited[i] = False

def permutation(n):
    result = [0] * m
    visited = [False] * n
    l = [(i + 1) for i in range(n)]
    perm(0, result, visited)

# combination 순서 없음
c_result = [0]*m
def comb(l, m, level, idx):
    if level == m:
        print(c_result)
        return
    for i in range(idx, len(l)):
        c_result[level] = l[i]
        comb(l, m, level+1, i+1)

# permutation = 순열 (순서 있음)
p_result = [0]*m
p_visited = [False]*len(l)
def permutation(l, m, level):
    if level == m:
       print(p_result)
       return
    for i in range(len(l)):
        if p_visited[i] == False:
            p_visited[i] = True
            p_result[level] = l[i]
            permutation(l, m, level+1)
            p_visited[i] = False

# combination = 조합 (순서없음)
c_result = [0]*m
def combination(l, m, level, idx):
    if level == m:
        print(c_result)
        return
    for i in range(idx, len(l)):
        c_result[level] = l[i]
        combination(l, m, level+1, i+1)

permutation(l, m, 0)
print('\\')
combination(l, m, 0, 0)
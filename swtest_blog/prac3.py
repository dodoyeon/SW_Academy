n = 5
m = 3
l = [(i+1) for i in range(n)]
result_p = [0]*m
visited_p = [False]*n
result_c =[0]*m
# visited_c = [False]*n

def permutation(l, m, level):
    if level == m:
        print(result_p)
        return
    for i in range(len(l)):
        if visited_p[i] == False:
            visited_p[i] = True
            result_p[level] = l[i]
            permutation(l,m,level+1)
            visited_p[i] = False

def combination(l, m, level, idx):
    if level == m:
        print(result_c)
        return
    for i in range(idx, len(l)):
        result_c[level] = l[i]
        combination(l, m, level+1, i+1)

# permutation(l,m,0)
# combination(l,m,0,0)

# 전역변수 초기화 필요!
result_p =[0]*m
visited_p= [False]*n
result_c =[0]*m
visited_c = [False]*n

# 중복 순열 (중복 허용)
result = []
def overlap_perm(l,m,level):
    if level == m:
        print(result_p)
        result.append(result_p)
        return
    for i in range(len(l)):
        if visited_p[i] == False:
            result_p[level] = l[i]
            overlap_perm(l,m,level+1)

# overlap_perm(l,m,0)
# print(len(result))

result = []
# 중복 조합 (중복 허용)
def overlap_comb(l,m,level, idx):
    if level == m:
        print(result_c)
        result.append(result_c)
        return
    for i in range(idx, len(l)):
        result_c[level] = l[i]
        overlap_comb(l,m,level+1, i)

# overlap_comb(l,m,0,0)
# print(len(result))

# 백준 15651
n, m = map(int, input().split())
l = [(i + 1) for i in range(n)]
result = [0] * m
visited = [False] * n

def over_comb(l, n, m, level):
    if level == m:
        print(' '.join(str(i) for i in result))
        return
    for i in range(n):
        # if visited[i] ==False:
        result[level] = l[i]
        over_comb(l, n, m, level + 1)

over_comb(l, n, m, 0)
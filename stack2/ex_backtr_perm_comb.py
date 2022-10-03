import itertools
n = 4
m = 3
l = [1, 2, 3, 4]

# # 라이브러리를 사용한 permutation (순서있음)
# for i in itertools.permutations(l, m):
#     print(i, end=" ")
#
# # 라이브러리를 사용한 combination
# for i in itertools.combinations(l, m):
#     print(i, end=' ')

# 라이브러리 없이 백트래킹 구현
result = [0]*m
check = [False]*len(l)

def permutation(l,m,level):
    if level == m: # M개 뽑은 경우
        print(result)
        return
    for i in range(len(l)): # n 개 중에서
        if check[i] == False:
            check[i] = True
            result[level] = l[i]
            permutation(l, m, level+1)
            check[i] = False # 이거 없으면 중복 허용

permutation(l, m, 0)

result = [0]*m
checked = [False]*len(l)

def combination(l, m, level, idx):
    if level == m:
        print(result)
        return
    for i in range(idx, len(l)):
        result[level] = l[i]
        combination(l, m, level+1, idx+1)
# 1182 부분 수열의 합
def combination(slist, n, s, l,level, idx):
    global k
    global num
    if level == l:
        if sum(num) == s:
            k += 1
        return
    for i in range(idx, n):
        num[level] = slist[i]
        combination(slist, n, s, l, level+1, i+1)
    return

def same(slist, n, s):
    global k
    global num
    k = 0
    for i in range(1, n+1):
        num = [0]*i
        combination(slist, n, s, i, 0, 0)

n, s = map(int, input().split())
su = list(map(int, input().split()))

same(su, n, s)
print(k)

# 순열과 조합 다시 외우기
p_result = [0]*m # 결과물
p_visited = [False]*len(l)
p = []
# 순열 : 순서있음
def permutation(l, m, level):
    if level == m:
        p.append(p_result)

    for i in range(len(l)):
        if p_visited[i] == False:
            p_visited[i] = True
            p_result[level] = l[i]
            permutation(l, m, level+1)
            p_visited[i] = False

c_result=[0]*m
c = []
# 조합 : 순서없음
def combination(l, m, level, idx):
    if level == m:
        c.append(c_result)
    for i in range(idx, len(l)):
        c_result[level] = l[i]
        combination(l, m, level+1, i+1)
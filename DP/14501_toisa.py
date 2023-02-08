# 퇴사 : 오늘의코테목표=리컬션마스터
# recursion 은 stack 이용 = 결국 D(깊이)FS = back tracking
def dfs(now, psum):
    global m
    if now == n:
        m = max(m, psum)
        return
    t, p = plist[now]
    if n >= now+t:
        dfs(now+t, psum+p)
    dfs(now+1, psum)

def dp(n, t, p):
    dpmem = [0 for i in range(n+1)]
    for i in range(len(t)-2, -1, -1):
        if t[i]+i <= n:
            dpmem[i] = max(p[i]+dpmem[i+t[i]], dpmem[i+1])
        else:
            dpmem[i] = dpmem[i+1]
    return dpmem[0]

n = int(input())
# plist = [list(map(int, input().split())) for _ in range(n)]
t = [0 for _ in range(n+1)]
p = [0 for _ in range(n+1)]
for i in range(n):
    a, b = map(int, input().split())
    t[i] = a
    p[i] = b
m = 0
# dfs(0, 0)
# print(m)
print(dp(n, t, p))
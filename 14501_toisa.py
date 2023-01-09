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

def dp()

n = int(input())
plist = [list(map(int, input().split())) for _ in range(n)]
m = 0
dfs(0, 0)
print(m)
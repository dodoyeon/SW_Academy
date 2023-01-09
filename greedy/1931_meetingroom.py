# 회의실 배정
def dfs(now, num):
    global m
    if now == n:
        m = max(m, num)
        
    if (now+)<=n:
        dfs(, num +1)
    dfs(, num)

n = int(input())
for i in range(n):
    s, e = map(int, input().split())
    meeting = [list(s, (e-s))]
m = 0
dfs(0, 0)
print()
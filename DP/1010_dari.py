# 다리 놓기
def dfs(now):
    global num
    if now == n:
        num += 1
        return
    for i in range(m):
        if i >= now:
            dfs(now+1)

def bridge(n, m):
    d=[]

    return

t = int(input())
num = 0
for _ in range(t):
    n, m = map(int, input().split())
    # dfs(0)
    # print(num)
    print(bridge(n, m))
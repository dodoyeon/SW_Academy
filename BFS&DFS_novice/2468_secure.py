# 안전지대
from collections import deque
n = int(input())
mapp = [list(map(int, input().split())) for _ in range(n)]
dx = (1,0,-1,0)
dy = (0,-1,0,1)

def bfs(mapp, visited, start, n, rain):
    q = deque()
    q.append(start)
    while bool(q):
        x, y  = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and visited[ny][nx] == False:
                visited[ny][nx] = True
                if mapp[ny][nx] > rain:
                    q.append([nx, ny])

def cal_bfs(mapp, visited, n, rain):
    num = 0
    for i in range(n):
        for j in range(n):
            if visited[j][i] == False and mapp[j][i] > rain:
                bfs(mapp, visited, (i, j), n, rain)
                num += 1
    return num

def cal(mapp, n):
    m = max(max(mapp))
    result = 1
    for i in range(1, m):
        visited = [[False] * n for _ in range(n)]
        ans = cal_bfs(mapp, visited, n, i)
        if result < ans:
            result = ans
    print(result)

cal(mapp, n)
# 영역 구하기
from collections import deque

dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)

def dfs(mapp, visited, start_x, start_y):
    q = deque()
    num = 1
    q.append([start_x, start_y])
    visited[start_y][start_x] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and visited[ny][nx] == False and mapp[ny][nx] == 0:
                q.append([nx, ny])
                visited[ny][nx] = True
                num += 1
    return num

def dfs_all(mapp, m, n):
    visited = [[False]*n for _ in range(m)]
    ans = []
    for i in range(n):
        for j in range(m):
            if mapp[j][i] == 0 and visited[j][i] == False:
                num = dfs(mapp, visited, i, j)
                ans.append(num)
    return ans

m, n, k = map(int, input().split())
mapp = [[0]*n for _ in range(m)]
for _ in range(k):
    ldx, ldy, rux, ruy = map(int, input().split())
    for i in range(ldx, rux):
        for j in range(ldy, ruy):
            mapp[j][i] = 1

ans = dfs_all(mapp, m, n)
ans.sort()
print(len(ans))
print(' '.join(str(i) for i in ans))
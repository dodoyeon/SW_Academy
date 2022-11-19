# 토마토
from collections import deque
dx = (1, 0, -1, 0, 0, 0)
dy = (0, 1, 0, -1, 0, 0)
dz = (0, 0, 0, 0, 1, -1)
def dfs(mapp, visited):
    q = deque()
    visited[0][0][0] = 0
    while q:
        x, y, z = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0<=x< and 0<=y< and 0<=z< and :
                visited[nz][ny][nx] = visited[z][y][x] + 1
    return visited[z][y][x]

m, n, h = map(int, input().split())
mapp = [list(map(int, input().split())) for _ in range(h)]
visited = [[-1] *  for _ in range(h)]
print(dfs(mapp, visited))
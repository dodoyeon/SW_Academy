# 토마토 -> dfs 가 아니라 bfs 로 풀어야 한다!! (엥 bfs 로 풀고있엇는디)
from collections import deque
dx = (1, 0, -1, 0, 0, 0)
dy = (0, 1, 0, -1, 0, 0)
dz = (0, 0, 0, 0, 1, -1)

def bfs(mapp, visited, q, m, n, h):
    while q:
        x, y, z = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0<=nx<m and 0<=ny<n and 0<=nz<h and mapp[nz][ny][nx] == 0 and visited[nz][ny][nx] == -1:
                visited[nz][ny][nx] = visited[z][y][x] + 1
                mapp[nz][ny][nx] = 1
                q.append([nx, ny, nz])

def search_bfs(mapp, visited, m, n, h):
    q = deque()
    for k in range(h):
        for j in range(n):
            for i in range(m):
                if mapp[k][j][i] == 1 and visited[k][j][i] == -1:
                    q.append([i,j,k])
    bfs(mapp, visited, q, m, n, h)


def write_res(mapp):
    m = -1
    for k in range(h):
        for j in range(n):
            if 0 in mapp[k][j]:
                return -1
            temp = max(visited[k][j])
            if m < temp:
                m = temp
    return m+1

m, n, h = map(int, input().split())
visited = []
mapp = []
for _ in range(h):
    mapp.append([list(map(int, input().split())) for _ in range(n)])
    visited.append([[-1] * m for _ in range(n)])
search_bfs(mapp, visited, m, n, h)

print(write_res(mapp))
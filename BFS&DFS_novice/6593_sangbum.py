# 상범 빌딩
from collections import deque
dx = (-1, 0, 1, 0, 0, 0)
dy = (0, -1, 0, 1, 0, 0)
dz = (0, 0, 0, 0, 1, -1)
def bfs(mapp, visited, start, end):
    q = deque()
    visited[start[2]][start[1]][start[0]] = 0
    q.append(start)
    while q:
        now = q.popleft()
        for i in range(6):
            nx = now[0] + dx[i]
            ny = now[1] + dy[i]
            nz = now[2] + dz[i]
            if 0<=nx<c and 0<=ny<r and 0<=nz<l and visited[nz][ny][nx] == -1 and (mapp[nz][ny][nx] == '.' or mapp[nz][ny][nx] == 'E'):
                q.append([nx, ny, nz])
                visited[nz][ny][nx] = visited[now[2]][now[1]][now[0]] + 1
    return visited[end[2]][end[1]][end[0]]

while True:
    l, r, c = map(int, input().split())  # 층, 행, 렬
    if l == 0 and c == 0 and r == 0:
        break
    mapp = []
    visited = []
    for i in range(l):
        layer = []
        for j in range(r):
            line = list(input())
            layer.append(line)
            for k in range(c):
                if line[k] == 'S':
                    start = [k, j, i]
                elif line[k] == 'E':
                    end = [k, j, i]
            visited.append([[-1]*c for _ in range(r)])
        mapp.append(layer)
        input()

    ans = bfs(mapp, visited, start, end)
    if ans == -1:
        print('Trapped!')
    else:
        print('Escaped in {} minute(s).'.format(ans))
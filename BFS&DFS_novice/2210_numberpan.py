# 숫자판 점프 = 중복순열
from collections import deque
dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

def dfs(mapp, visited):
    q = deque()
    q.append([0,0])
    visited[0][0] = 0
    while q:
        length = 0
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=x<5 and 0<=y<5 and visited[ny][nx] ==False:
                q.append([nx, ny])
                visited[ny][nx] = visited[y][x] + 1
            if visited[ny][nx] == 6:

    return
mapp = [list(map(int, input().split())) for _ in range(5)]
visited = [[False] * 5 for _ in range(5)]
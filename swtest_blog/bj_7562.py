from collections import deque
dx=[-2,-1,2,1,2,1,-2,-1]
dy=[1,2,1,2,-1,-2,-1,-2]

def bfs(sx,sy,ex,ey, l):
    visited = [[0] * l for _ in range(l)]
    q = deque()
    q.append([sx,sy])
    visited[sy][sx] = 1
    while bool(q):
        x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<l and 0<=ny<l and visited[ny][nx]==0:
                visited[ny][nx] = visited[y][x]+1
                q.append([nx,ny])
        # if nx == ex and ny == ey:
        #     print(visited[ny][nx]-1)
    print(visited[ey][ex] - 1)

t = int(input())
for _ in range(t):
    l = int(input())
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    bfs(sx,sy, ex,ey, l)
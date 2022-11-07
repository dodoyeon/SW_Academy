# Breadth First Search 너비 우선 탐색 = Queue 이용
from collections import deque
def bfs(graph, n, start):
    q = deque()
    visited = [False]*n
    q.append(start)
    visited[start] = True
    while bool(q):
        now = q.popleft()
        print(now, end=" ")
        for v in graph[now]:
            if visited[v] == False:
                visited[v] = True
                q.append(v)


def bfs_xycoor(x, y, n):
    dx = (1,0,-1,0)
    dy = (0,-1,0,1)
    q = deque()
    visited = [[False]*n for _ in range(n)]
    q.append([x,y])
    visited[y][x] = True
    while bool(q):
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<n and visited[ny][nx]==False:
                visited[ny][nx] = True
                q.append([nx,ny])
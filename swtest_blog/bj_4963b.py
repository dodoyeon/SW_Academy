from collections import deque
# 섬의 개수
dx = [1,0,-1,0,1,-1,1,-1]
dy = [0,1,0,-1,1,-1,-1,1]
def search_all(mapp, w, h):
    num = 0
    visited = [[False] * w for _ in range(h)]
    for x in range(w):
        for y in range(h):
            if mapp[y][x] == 1 and visited[y][x] == False:
                bfs(x,y,mapp, visited, w, h)
                num += 1
            visited[y][x] = True
    print(num)

def bfs(x,y,mapp,visited, w, h):
    q = deque()
    q.append([x,y])
    visited[y][x] = True

    while bool(q):
        x,y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<w and 0<=ny<h and mapp[ny][nx]==1 and visited[ny][nx]==0:
                q.append([nx, ny])
                visited[ny][nx] = True

while True:
    w,h = map(int, input().split())
    if w == 0 and h == 0:
        break
    mapp = [list(map(int, input().split())) for _ in range(h)]
    search_all(mapp,w,h)
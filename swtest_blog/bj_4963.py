from collections import deque
def dfs(x,y, level):
    global dx
    global dy
    global visited
    if
        return
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<=w and 0<=ny<=h and visited[nx][ny] == 0:
            dfs(nx, ny)


while True:
    w, h = map(int, input().split())
    if w ==0 and h ==0:
        break
    mapp = [list(map(int, input().split())) for _ in range(h)]

    visited = [[0]*w for _ in range(h)]
    dx = [1,0,-1,0,1,1,-1,-1]
    dy = [0,1,0,-1,1,-1,-1,1]


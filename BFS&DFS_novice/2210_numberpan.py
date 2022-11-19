# 숫자판 점프 = 중복순열
from collections import deque
dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

def dfs(mapp):
    q = deque()
    q.append([0,0])
    check = []
    while q:
        length = 1

        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=x<5 and 0<=y<5:
                q.append([nx, ny])
                length += 1
            if length == 6:

    return
mapp = [list(map(int, input().split())) for _ in range(5)]
# 병든 나이트
dx = (1, 2, -1, -2)
dy = (2, 1, 2, 1)
max_n = 0
def dfs(visited, num, x, y):
    global dx, dy
    global max_n
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx < m and 0 <= ny < n and visited[ny][nx] == False:
            num[i] += 1
            visited[ny][nx] = True
            dfs(visited, num, nx, ny)
    if 0 in num:
        pass
    else:
        s = sum(num)
        if max_n < s:
            max_n = s

def move(n, m):
    visited = [[False]*m for _ in range(n)]
    num = [0]*4
    dfs(visited, num, 0, 0)

n, m = map(int, input().split())
move(n, m)
print(max_n)
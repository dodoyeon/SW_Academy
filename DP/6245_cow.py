# Cow Solitaire
# from collections import deque -> BFS 아니고 DFS 여야한다.
def recur(x, y, d, visited):
    global dx, dy, score
    if visited[y][x] == 2 * n - 1:
        return
    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and visited[ny][nx] == 0:
            d[ny][nx] = max(d[y][x] + score[mapp[ny][nx][0]], d[ny][nx])
            visited[ny][nx] = visited[y][x] + 1
            recur(nx, ny, d, visited)
            visited[ny][nx] = 0

def cow(n, mapp, start):
    global dx, dy, score
    dx = (1, 0)
    dy = (0, -1)
    l = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
    score = {cha: (i+1) for i, cha in enumerate(l)}
    visited = [[0]*n for _ in range(n)]
    visited[n-1][0] = 1
    d = [[0]*n for _ in range(n)]
    d[n-1][0] = score[mapp[n-1][0][0]]
    recur(0, n-1, d, visited)
    maxn = 0
    for i in range(n):
        maxn = max(maxn, max(d[i]))
    return maxn

n = int(input())
mapp = [list(input().split()) for _ in range(n)]
print(cow(n, mapp, (n-1, 0)))
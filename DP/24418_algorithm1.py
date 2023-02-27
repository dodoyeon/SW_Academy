# 알고리즘 수업 - 행렬경로문제 1
def recur(m, n, x, y):
    global visited, dx, dy, num
    for i in range(2):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<n and 0<=ny<n:
            visited[ny][nx] = max(visited[y][x] + m[ny][nx], visited[ny][nx])
            num += 1
            recur(m, n, nx, ny)

def dfs(m, n, x, y):
    global visited, dx, dy, num
    visited = [[0]*n for _ in range(n)]
    visited[0][0] = m[0][0]
    dx = (1, 0)
    dy = (0, 1)
    num = 1
    recur(m, n, x, y)
    return num+1 #, visited[n-1][n-1]

def dp(m, n):
    d = [[0]*n for _ in range(n)]
    num2 = 0
    d[0][0] = m[0][0]
    for i in range(n):
        for j in range(n):
            num2 += 1
            if i == 0 and j == 0:
                pass
            elif i == 0:
                d[j][i] = max(d[j][i], m[j][i] + d[j-1][i])
            elif j == 0:
                d[j][i] = max(d[j][i], m[j][i] + d[j][i-1])
            else:
                d[j][i] = max(d[j][i], m[j][i] + d[j-1][i], m[j][i]+d[j][i-1])
    return num2 #, d[n-1][n-1]

def num_compare(n):
    d = [[0] * n for _ in range(n)]
    num = 2*n-1
    for i in range(n):
        d[0][i] = 1
    for i in range(1, n):
        d[i][0] = 1
    for i in range(1, n):
        for j in range(1, n):
            d[j][i] = d[j-1][i]+d[j][i-1]
            num += d[j][i]
    return num +1, n**2

n = int(input())
m = [list(map(int, input().split())) for _ in range(n)]
# print(dfs(m, n, 0, 0), end=' ')
# print(dp(m, n))
print(*num_compare(n), sep=' ')
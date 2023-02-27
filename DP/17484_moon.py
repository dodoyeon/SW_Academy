# 진우의 달 여행 (small)
# n, m = map(int, input().split())
# l = [list(map(int, input().split())) for _ in range(n)]

def recur(x, y, idx):
    global d, dx, dy
    for i in idx:
        px, py = x+dx[i], y+dy[i]
        if 0<=px<m and 0<=py<n:
            pidx = [j for j in range(3) if j != i]
            if py < n-1:
                d[py][px] = d[y][x] + l[py][px]
                recur(px, py, pidx)
            elif py == n-1:
                if d[py][px] == 0:
                    d[py][px] = d[y][x] + l[py][px]
                else:
                    d[py][px] = min(d[py][px], d[y][x] + l[py][px])

def moon():
    global d, dx, dy
    d = [[0]*m for _ in range(n)]
    for i in range(m):
        d[0][i] = l[0][i]
    dx = (0, 1, -1)
    dy = (1, 1, 1)
    idx = [i for i in range(3)]
    for i in range(m):
        recur(i, 0, idx)
    return min(d[n-1])

# print(moon())

# moon_answersheet
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0,0,0] for _ in range(M)]] + [[[float('inf'),float('inf'),float('inf')] for _ in range(M)] for _ in range(N)]

for i in range(1,N+1):
    for j in range(M):
        if j < M-1:
            dp[i][j][0] = min(dp[i-1][j+1][1],dp[i-1][j+1][2]) + matrix[i-1][j]
        if 0 < j:
            dp[i][j][2] = min(dp[i-1][j-1][1],dp[i-1][j-1][0]) + matrix[i-1][j]
        dp[i][j][1] = min(dp[i-1][j][0],dp[i-1][j][2]) + matrix[i-1][j]

min_value = float('inf')
for row in dp[i]:
    for each in row:
        min_value = min(min_value,each)
print(min_value)
# Hexagonal tiles
# recursive  하니까 시간초과 뜬다..
def recur(x, y, n, visited):
    global dx, dy, num, colen, mok, nam
    if x == mok and y != nam:
        num += 1
        return
    for i in range(3):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<colen and 0<=ny<2 and visited[ny][nx] == False:
            visited[ny][nx] = True
            recur(nx, ny, n, visited)
            visited[ny][nx] = False

def hex(n):
    global dx, dy, num, colen, mok, nam
    dx = (1, 0, 1)
    dy = (0, -1, 1)
    colen = ((n+1)//2+(n+1)%2)
    visited = [[False]*colen for _ in range(2)]
    visited[1][0] = True
    mok, nam = n//2, n%2
    if nam == 0:
        visited[0][colen-1] = True
    num = 0
    recur(0, 1, n, visited)
    return num

def hex2(n):
    if n < 3:
        return n
    colen = ((n + 1) // 2 + (n + 1) % 2)
    d = [[0] * colen for _ in range(2)]
    d[0][0], d[1][1] = 1, 2
    mok, nam = n // 2, n % 2
    for i in range(colen):
        for j in range(1, -1, -1):
            if (i == 1 and j == 1) or (i == 0 and j == 0) or (i == 0 and j == 1):
                pass
            elif j == 1:
                d[j][i] = d[j-1][i-1]+d[j][i-1]
            else:
                d[j][i] = d[j+1][i] + d[j][i-1]
    if nam == 0:
        return d[1][mok]
    else:
        return d[0][mok]

while True:
    n = int(input())
    if n == 0:
        break
    print(hex2(n))
# 병든 나이트
dx = (1, 2, 1, 2)
dy = (2, 1, -2, -1)
def bfs(visited, num, x, y): # 이런식으로 푸는 문제가 아니다!!!
    global dx, dy
    global max_n
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx < m and 0 <= ny < n and visited[ny][nx] == False:
            num[i] += 1
            visited[ny][nx] = True
            num = bfs(visited, num, nx, ny)
    s = sum(num)
    if (0 in num) and s >= 4:
        return sum(sum(i) for i in visited)
        # return visited.count(True)
    elif s < 4:
        return sum(sum(i) for i in visited)
    else:
        return 1
def move(n, m):
    visited = [[False]*m for _ in range(n)]
    num = [0]*4
    visited[0][0] = True
    return bfs(visited, num, 0, 0)

def greedy(n, m):

n, m = map(int, input().split())
print(greedy(n, m))
from collections import deque
# DFS 로 풀면 recursion error 가 뜨는데
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def search_all(n, m, pic):
    num = 0
    maxn = 0
    visited = [[False] * m for _ in range(n)]

    for x in range(m):
        for y in range(n):
            if pic[y][x] == 1 and visited[y][x]==False:
                big = bfs_pic(x, y, pic, visited)
                num += 1
                if big > maxn:
                    maxn = big
            visited[y][x] = True
    print(num)
    print(maxn)

def bfs_pic(x,y,pic,visited):
    q = deque()
    q.append([x,y])
    big = 1
    visited[y][x] = True

    while bool(q):
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and visited[ny][nx] == False and pic[ny][nx] == 1:
                q.append([nx,ny])
                visited[ny][nx] = True
                big += 1
    return big

n, m = map(int, input().split())
pic = [list(map(int, input().split())) for _ in range(n)]
search_all(n, m, pic)
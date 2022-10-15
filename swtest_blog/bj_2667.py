from collections import deque
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(mapp, visited, x, y):
    q = deque()
    q.append([x,y])
    num = 1
    while q:
        x, y =q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and mapp[ny][nx]==1 and visited[ny][nx]==0:
                visited[ny][nx] = 1
                q.append([nx,ny])
                num += 1
    return num

def dangi(mapp, n):
    visited = [[0] * n for _ in range(n)]
    vil = []

    for i in range(n):
        for j in range(n):
            if mapp[j][i] == 1 and visited[j][i]==0:
                visited[j][i] = 1
                num = bfs(mapp, visited,i, j)
                vil.append(num)
            visited[j][i] = 1
    return vil

n = int(input())
mapp = [list(map(int, input())) for _ in range(n)]
vil = dangi(mapp, n)
print(len(vil))
vil.sort()
for item in vil:
    print(item)
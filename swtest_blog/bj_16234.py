from collections import deque
# 인구이동
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(a,visited,mapp,n,l,r,x,y):
    q = deque()
    q.append([x,y])
    visited[y][x] = True
    # mapp[y][x] = True
    index = [(x,y)]
    sum = a[y][x]
    num = 1
    stop = 0

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[ny][nx]:
                if l<=abs(a[ny][nx]-a[y][x])<=r:
                    sum += a[ny][nx]
                    num += 1
                    stop += 1
                    q.append([nx,ny])
                    visited[ny][nx] = True
                    # mapp[ny][nx] = True
                    index.append((nx,ny))
    value = (sum//num)
    for x,y in index:
        mapp[y][x] = value

    return value, stop

def search(a,n,l,r):
    visited = [[False] * n for _ in range(n)]
    mapp = [[0]*n for _ in range(n)]
    stop2 = 0

    for j in range(n):
        for i in range(n):
            if not visited[j][i]:
                value, stop = bfs(a,visited,mapp,n,l,r,i,j)
                # for c in range(n):
                #     for d in range(n):
                #         if mapp[d][c]:
                #             mapp[d][c] = value
                stop2 += stop
    return mapp, stop2

def search_all(a,n,l,r):
    often = 0
    stop = 1
    while stop != 0:
        mapp, stop = search(a,n,l,r)
        often += 1
        a = mapp
    print(often-1)

n, l, r = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
search_all(a,n,l,r)
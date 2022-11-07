# 맥주 마시면서 걸어가기
# 왜 너비 우선 탐색이지..? 깊이가 아니라? ㅠㅜ
from collections import deque
def bfs(start, conv, end, n):
    visited = [False]*n
    q = deque()
    q.append(start)
    while bool(q):
        nx, ny = q.popleft()
        dist = abs(nx - end[0]) + abs(ny - end[1])
        if dist <= 1000:
            return 'happy'
        for i in range(n):
            nc = conv[i]
            dist = abs(nx-nc[0]) + abs(ny-nc[1])
            if dist <= 1000 and visited[i] == False:
                visited[i] = True
                q.append(nc)
    return 'sad'

t = int(input())
for _ in range(t):
    n = int(input())  # 편의점개수
    start = list(map(int, input().split()))
    conv = [list(map(int, input().split())) for _ in range(n)]
    end = list(map(int, input().split()))
    print(bfs(start, conv, end, n))
from collections import deque
def bfs(n, k):
    q = deque()
    visited = [-1] * 100001
    q.append(n)
    visited[n] = 0
    while bool(q):
        node = q.popleft()
        if node == k:
            return visited[k]
        for i in range(3):
            if i == 0:
                new = node + 1
            elif i == 1:
                new = node - 1
            else:
                new = 2*node
            if 0<=new<=100000 and visited[new] == -1:
                visited[new] = visited[node]+1
                q.append(new)

n, k = map(int, input().split())
print(bfs(n, k))
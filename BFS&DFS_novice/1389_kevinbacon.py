# 케빈 베이컨의 6단계 법칙
from collections import deque
def bfs(graph, start, n):
    q = deque()
    visited = [-1] * n
    visited[start-1] = 0
    q.append(start)
    while q:
        node = q.popleft()
        for new in graph[node-1]:
            if visited[new-1] == -1:
                visited[new-1] = visited[node-1]+1
                q.append(new)
    return visited

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1].append(b)
    graph[b-1].append(a)

num = 5000
min = []
for i in range(1, n+1):
    ans = bfs(graph, i, n)
    bacon = 0
    for j in ans:
        if j != -1:
           bacon += j
    min.append(bacon)
    if bacon < num:
        num = bacon

for i in range(n):
    if min[i] == num:
        print(i+1)
        break
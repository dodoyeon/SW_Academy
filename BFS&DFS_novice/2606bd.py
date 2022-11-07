# 바이러스
from collections import deque
v = int(input())
e = int(input())
graph = [[] for _ in range(v)]
# graph = [[1,2,3],[1],[23,4]]
for _ in range(e):
    x, y = map(int, input().split())
    graph[x-1].append(y)
    graph[y-1].append(x)

def bfs(graph, start, v):
    num = 0
    q = deque()
    visited = [False]*v
    visited[start-1] = True
    q.append(start)
    while bool(q):
        now = q.popleft()
        for node in graph[now-1]:
            if visited[node-1] == False:
                visited[node-1] = True
                q.append(node)
                num += 1
    return num

def dfs_recur(graph, node, visited):
    global num
    visited[node-1] = True
    for new in graph[node-1]:
        if visited[new-1] == False:
            num += 1
            dfs_recur(graph, new, visited)

def dfs(graph, start, v):
    visited = [False]*v
    dfs_recur(graph, start, visited)
    return num

# print(bfs(graph, 1, v))
num = 0
print(dfs(graph, 1, v))
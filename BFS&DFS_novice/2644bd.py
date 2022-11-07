# 촌수계산 : 근데 BFS 보다는 DFS 가 더 효과적일 것 같다.
from collections import deque
n = int(input())
tar_x, tar_y =map(int, input().split())
m = int(input())
tree = [[] for _ in range(n)]
for _ in range(m):
    x, y = map(int, input().split())
    tree[x-1].append(y)
    tree[y-1].append(x)

def bfs(graph, target, start, n):
    q = deque()
    visited = [-1]*n
    q.append(start)
    # visited[start-1] = True
    while q:
        now = q.popleft()
        for node in graph[now-1]:
            if visited[node-1] == -1:
                visited[node - 1] = visited[now-1]+1
                q.append(node)
    return visited[target-1]

def dfs_recur(graph, node, target, visited):
    # if node == target:
    #     return

    for new in graph[node-1]:
        if visited[new-1] == -1:
            visited[new - 1] = visited[node-1]+1
            dfs_recur(graph, new, target, visited)

def dfs(graph, tar_x, tar_y, n):
    visited = [-1] * n
    dfs_recur(graph, tar_y, tar_x, visited)
    return visited[tar_x-1]

# DFS 풀이
ans = dfs(tree, tar_x, tar_y, n)

# BFS 풀이
# ans = bfs(tree, tar_x, tar_y, n)
if ans != -1:
    print(ans+1)
else:
    print(ans)
from collections import deque
# DFS
def dfs_recur(graph, node, visited):
    visited[node] = True #재귀이므로 visited 바로 넣음
    print(node, end=" ")

    for nextn in graph[node]:
        if visited[nextn] == False: # 현재 노드의 새끼 노드를 재귀 처리
            dfs_recur(graph, nextn, visited)

def dfs(graph, n, start):
    visited=[False]*(n+1)
    dfs_recur(graph, start, visited)

# BFS : 너비 우선 탐색
def bfs(graph,n, start):
    visited = [False]*(n+1) # visited 는 안에 생성!
    q = deque() # deque 는 빠르다 -> bfs는 큐를 사용
    q.append(start)
    visited[start] = True # visited 도 바로 넣기

    while bool(q): # 큐가 비어있지 않는 동안
        now = q.popleft() # 큐는 popleft() 사용한다
        print(now, end=" ")
        for node in graph[now]: # 현재노드의 새끼노드를 처리
            if visited[node] == False:
                visited[node] = True
                q.append(node)

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

dfs(graph, n, v)
print()
bfs(graph, n, v)
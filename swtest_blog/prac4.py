# DFS 와 BFS
from collections import deque
#백준 1260

# 그래프 인풋을 표현하는 법 : 1. 인접행렬 방식 약간 비효율적
# n,m,v = map(int, input().split()) #노드, 엣지, 시작노드
# graph = [[0]*n for _ in range(n)]
# for i in range(m):
#     a,b = map(int, input().split())
#     graph[(a-1)][(b-1)] = 1
#     graph[(b - 1)][(a - 1)] = 1
# print(graph)

# 2. 인접 리스트 방식
n,m,v = map(int, input().split())
graph_2 = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph_2[a].append(b)
    graph_2[b].append(a)
# print(graph_2)

for i in graph_2:
    i.sort()


def BFS(graph,n, start): # 너비 우선 탐색 : 큐와 visited 리스트 사용
    visited_bfs = [False] * (n + 1)
    q = deque()
    q.append(start)
    visited_bfs[start] = True

    while bool(q):
        now = q.popleft()
        print(now, end=" ")
        for node in graph[now]:
            if visited_bfs[node] == False:
                visited_bfs[node] = True
                q.append(node)

def DFS_recursive(graph, node, visited): # 깊이우선 탐색 : stack 과 재귀사용
    visited[node] = True
    print(node, end=" ")

    for nextn in graph[node]:
        if visited[nextn] == False:
            DFS_recursive(graph, nextn, visited)

def DFS(graph, n, start):
    visited = [False]*(n+1)
    DFS_recursive(graph, start, visited)

def DFS_stack(graph,n, start):
    visited_dfs = [False] * (n + 1)
    stack = deque()
    stack.append(start)

    while bool(stack):
        now = stack.pop()

        if visited_dfs[now] == False:
            visited_dfs[now] = True
            print(now, end=" ")
            for i in range(len(graph[now])-1, 0, -1):
                stack.append(graph[now][i])

DFS_stack(graph_2,n,v) # 틀림
print('\n')
DFS(graph_2, n, v)
print('\n')
BFS(graph_2,n,v)

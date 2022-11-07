# Depth First Search 깊이 우선 탐색 = Stack 이용 / Recursion 이용 (o)

def dfs_recur(graph, node, visited):
    visited[node] = True
    print(node, end=" ")

    for nextn in graph[node]:
        if visited[nextn] == False:
            dfs_recur(graph, node, visited)

def dfs(graph, n, start):
    visited = [False] * n
    dfs_recur(graph, start, visited)
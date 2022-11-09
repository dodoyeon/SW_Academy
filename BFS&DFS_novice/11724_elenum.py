# 연결 요소의 개수
from collections import deque
import sys # 정말 complexity 를 줄이기 위해서 이거밖에 방법이 없는건가??????

def bfs(graph, q, visited, start):
    q.append(start)
    visited[start-1] = True
    while q:
        node = q.popleft()
        for new in graph[node-1]:
            if not visited[new-1]:
                visited[new-1] = True
                q.append(new)

def cal_bfs(graph, n):
    num = 0
    q = deque()
    visited = [False] * n
    for i in range(1, n+1):
        if not visited[i-1]:
            bfs(graph, q, visited, i)
            num += 1
    return num

# n, m = map(int, input().split())
n, m = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    # u, v = map(int, input().split())
    u,v = map(int, sys.stdin.readline().rstrip().split())
    graph[u-1].append(v)
    graph[v-1].append(u)

print(cal_bfs(graph, n))
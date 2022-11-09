# 특정 거리의 도시 찾기
from collections import deque
import sys # 얘도 방법이 이거밖에 없는건가??????

def bfs(graph, visited, start, n):
    q = deque()
    q.append(start)
    visited[start-1] = 0
    num = []
    while q:
        node = q.popleft()
        # if visited[node-1] == k:
        #     num.append(node)
        for new in graph[node-1]:
            if visited[new-1] == -1:
                visited[new-1] = visited[node-1] + 1
                q.append(new)

# n, m, k, x = map(int, input().split())
n, m, k, x = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    v, u = map(int, sys.stdin.readline().rstrip().split())
    graph[v-1].append(u)

visited = [-1] * n
bfs(graph, visited, x, n)

check = False
for i in range(n):
    if visited[i] == k:
        print(i+1)
        check = True
if check == False:
    print(-1)

# if len(ans) == 0:
#     print(-1)
# else:
#     ans.sort()
#     for i in ans:
#         print(i)
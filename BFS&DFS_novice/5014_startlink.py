from collections import deque
def bfs(start, end, elev, n):
    q = deque()
    visited = [-1]*n
    q.append(start)
    visited[start-1] = 0
    while bool(q):
        node = q.popleft()
        for i in range(2):
            new = node+elev[i]
            if (1 <= new <= f) and (visited[new-1] == -1):
                visited[new-1] = visited[node-1]+1
                q.append(new)
    return visited[end-1]

f, s, g, u, d = map(int, input().split())
ans = bfs(s, g, [u, -d], f)
if ans == -1:
    print('use the stairs')
else:
    print(ans)
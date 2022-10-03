def DFS(conn, v, s, g):
    visited = []
    stack = [s]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(conn[node])

def find(conn, v, s, g):
    visited = []
    stack = [s]
    while stack:
        node = stack.pop()
        if node not in visited: # visited 아닌 애를 찾아서
            visited.append(node)
            if g in conn[node]:
                return 1
            stack.extend(conn[node])
    return 0
        
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    v, e = map(int, input().split()) # 노드개수, 엣지개수
    conn = {i+1:[] for i in range(v)}
    for i in range(e):
        a, b= map(int, input().split())
        conn[a].append(b)
    s, g = map(int, input().split())
    print('#{} {}'.format(test_case, find(conn, v, s, g)))
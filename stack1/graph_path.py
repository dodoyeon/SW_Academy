def find(conn, v, s, g):
    next = s
    visit = [0 for _ in range(v)]
    stack = []
    while next != g:
        if : # 다 visit 해봣으면

        visit[next] = 1
        if g in conn[next]:
            next = g
        else:
            for idx in conn[next]:
                ver = conn[next][idx]
                if visit[ver] != 1:
                    next = ver
                    stack.apppend(idx)
                else:

    return 1
        
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    v, e = map(int, input().split()) # 노드개수, 엣지개수
    conn = {i:[] for i in range(v)}
    for _ in range(e):
        s, e = map(int, input().split())
        conn[s].append(e)
    s, g = map(int, input().split())
    find(conn, v, s, g)
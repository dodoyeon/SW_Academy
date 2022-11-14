from collections import deque

def bfs(mapp, pos_s, pos_w):
    if len(pos_w) == 0:
        return mapp, 1
    for i in pos_s:
        for j in pos_w:
            sub = i-j
            if (sub[0]==0 and sub[1]==1) or (sub[1]==0 and sub[0]==1):
                return mapp, 0
    dx = (1, 0, -1, 0)
    dy = (0, 1, 0, -1)
    q = deque()
    for i in pos_s:
        q.append(i)
    while q:
        sheep = q.popleft()
        for i in range(4):
            nx = sheep[0] + dx[i]
            ny = sheep[1] + dy[i]
            if (nx, ny) in pos_w:
    return mapp, 1

    # for i in pos_s:
    #     for j in pos_w:
    #         if i[0] == j[0]:
    #
    #         elif i[1] == j[1]:

r, c = map(int, input().split())
pos_s = []
pos_w = []
mapp = []
for i in range(r):
    l = list(input())
    mapp.append(l)
    for j in range(c):
        if l[j] == 'S':
            pos_s.append([j, i])
        elif l[j] == 'W':
            pos_w.append([j, i])
ans_map, result = bfs(mapp, pos_s, pos_w)

print(result)
for i in ans_map:
    print("".join(j for j in i))
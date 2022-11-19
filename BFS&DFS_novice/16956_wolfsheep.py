def search_wolf(mapp, r, c):
    dx = (1, 0, -1, 0)
    dy = (0, 1, 0, -1)
    for i in range(c):
        for j in range(r):
            if mapp[j][i] == 'S':
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0<=nx<c and 0<=ny<r and mapp[ny][nx] != 'S':
                        if mapp[ny][nx] != 'W':
                            mapp[ny][nx] = 'D'
                        else:
                            return mapp, 0
    return mapp, 1

r, c = map(int, input().split())
mapp = [list(input()) for _ in range(r)]
# pos_s = []
# pos_w = []
# mapp = []
# for i in range(r):
#     l = list(input())
#     mapp.append(l)
#     for j in range(c):
#         if l[j] == 'S':
#             pos_s.append([j, i])
#         elif l[j] == 'W':
#             pos_w.append([j, i])
ans_map, result = search_wolf(mapp, r, c)

print(result)
if result == 1:
    for i in ans_map:
        print("".join(j for j in i))
else:
    pass
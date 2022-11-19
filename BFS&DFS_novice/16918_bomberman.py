# 봄버맨
def bomb(mapp, r, c, n):
    gonna = []
    dx = (1, 0, -1, 0)
    dy = (0, 1, 0, -1)
    for sec in range(2, n+1):
        if sec%2 == 0:
            for i in range(c):
                for j in range(r):
                    if mapp[j][i] == '.':
                        mapp[j][i] = 'O'
                    else:
                        gonna.append([i, j])
        else:
            while gonna:
                i, j = gonna.pop()
                mapp[j][i] = '.'
                for k in range(4):
                    nx = i+dx[k]
                    ny = j+dy[k]
                    if 0<=nx<c and 0<=ny<r:
                        mapp[ny][nx] = '.'
    return mapp

r, c, n = map(int, input().split())
mapp = [list(input()) for _ in range(r)]
ans = bomb(mapp, r, c, n)
for i in ans:
    print(''.join(j for j in i))
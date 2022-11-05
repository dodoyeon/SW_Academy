from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def jari(mn, n, student):
    mapp = [[0] * mn for _ in range(mn)]
    mapp[1][1] = student[0][0]
    man = 0 # 만족도
    for new in range(1, n):
        st = student[new][0]
        like = student[new][1:]
        result = []
        maxn = 0
        for y in range(mn):
            for x in range(mn):
                if mapp[y][x] == 0:
                    num = 0
                    binn = 0
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if 0 <= nx < mn and 0 <= ny < mn and mapp[ny][nx] in like:
                            num += 1
                        elif 0 <= nx < mn and 0 <= ny < mn and mapp[ny][nx] == 0:
                            binn += 1
                    if num > maxn:
                        maxn = num
                        result = [[x, y, num, binn]]
                    elif num == maxn:
                        result.append([x, y, num, binn])

        if len(result) > 1:
            maxn = 0
            like = []
            for i in result:
                v = i[-1]
                if maxn < v:
                    maxn = v
                    like = [i]
                elif v == maxn:
                    like.append(i)
            result = like
            if len(result) > 1:
                maxn = 20
                like = []
                for i in result:
                    v = i[1]
                    if maxn > v:
                        maxn = v
                        like = [i]
                    elif v == maxn:
                        like.append(i)
                result = like
                if len(result) > 1:
                    maxn = 20
                    like = []
                    for i in result:
                        v = i[0]
                        if maxn > v:
                            maxn = v
                            like = [i]
                        elif v == maxn:
                            like.append(i)
                    result = like
        mapp[result[0][1]][result[0][0]] = st
        if num >= 1:
            man += 10 ** (num - 1)
    return man

n = int(input())
m = n**2
student = [list(map(int, input().split())) for _ in range(m)]
print(jari(n, m, student))
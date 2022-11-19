b_num = 0
w_num = 0

def bfs(mapp, n):
    global w_num
    global b_num
    color = mapp[0][0]
    check = 0
    if n == 1:
        if color == 0:
            w_num += 1
        else:
            b_num += 1
        return
    for i in range(n):
        for j in range(n):
            if mapp[j][i] != color: # 이전칸이랑 색이다르면
                check = 1
                break # break 는 1개 for 문에만 적용된다.
        if check == 1:
            break
    if check == 1:
        half = n // 2
        for k in range(1, 3):
            for l in range(1, 3):  # 반반으로 자른 작은정사각형에 대한 포문
                new_mapp = [row[half * (k - 1):half * k] for row in mapp[half * (l - 1):half * l]]
                bfs(new_mapp, half)
    else:
        if color == 0:
            w_num += 1
        else:
            b_num += 1
        return

def origami(mapp, n):
    global w_num
    global b_num
    bfs(mapp, n)
    return [w_num, b_num]

n = int(input())
mapp = [list(map(int, input().split())) for _ in range(n)]

for i in origami(mapp, n):
    print(i, end='\n')
# 종이의 개수
num_m1 = 0
num_0 = 0
num_1 = 0
def bfs(mapp, n):
    global num_m1
    global num_0
    global num_1
    check_num = mapp[0][0]
    if n == 1:
        if check_num ==-1:
            num_m1 += 1
        elif check_num == 0:
            num_0 += 1
        else:
            num_1 += 1
        return

    check = False
    for i in range(n):
        for j in range(n):
            if mapp[j][i] != check_num:
                check = True
                break
        if check == True:
            break

    length = n // 3
    if check == True:
        for i in range(1, 4):
            for j in range(1, 4):
                new_mapp = [row[length*(j-1):length*j] for row in mapp[length*(i-1):length*i]]
                bfs(new_mapp, length)
    else:
        if check_num == -1:
            num_m1 += 1
        elif check_num == 0:
            num_0 += 1
        else:
            num_1 += 1
    return

def num_paper(mapp, n):
    global num_m1
    global num_0
    global num_1
    bfs(mapp, n)
    return [num_m1, num_0, num_1]

n = int(input())
mapp = [list(map(int, input().split())) for _ in range(n)]
for i in num_paper(mapp, n):
    print(i)
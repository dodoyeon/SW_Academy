# 7568 덩치
def dungchi(rlist, n):
    num = []
    k = 0
    for i in range(n):
        for j in range(n):
            me = rlist[i]
            you = rlist[j]
            if you[0] > me[0] and you[1]>me[1]:
                k += 1
        num.append(k)
        k = 0
    return num

n = int(input())
rlist = []
for _ in range(n):
    rlist.append(list(map(int, input().split())))

num = dungchi(rlist, n)
for i in num:
    print((i+1), end = ' ')
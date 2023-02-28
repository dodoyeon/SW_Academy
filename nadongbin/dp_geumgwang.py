# 금광
def gwang(n ,m ,l):
    d = [[0]*m for _ in range(n)]
    for i in range(n):
        d[i][0] = l[i][0]
    for i in range(1, m):
        for j in range(n):
            if j == (n-1):
                d[j][i] = max(d[j-1][i-1], d[j][i-1])+l[j][i]
            elif j == 0:
                d[j][i] = max(d[j+1][i-1], d[j][i-1])+l[j][i]
            else:
                d[j][i] = max(d[j-1][i-1], d[j][i-1], d[j+1][i-1])+l[j][i]
    return max([d[i][-1] for i in range(n)])

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    l = list(map(int, input().split()))
    new_l = []
    t = [l[0]]
    for i in range(1, len(l)):
        if i%m == 0:
            new_l.append(t)
            t = []
        t.append(l[i])
    new_l.append(t)
    print(gwang(n,m,new_l))
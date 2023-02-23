def toisa(n, l):
    d = [0]*n
    if l[-1][0] == 1:
        d[-1] = l[-1][1]
    for i in range(n-2, -1, -1):
        now = l[i]
        if (i+now[0]-1) <= n-1:
            d[i] = max(d[i+now[0]-1]+now[1], d[i])
        else:
            d[i] = d[i+1]
    return d[0]

n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
print(toisa(n, l))
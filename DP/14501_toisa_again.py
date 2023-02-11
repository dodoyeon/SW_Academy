def toisa(n, l):
    d = [0]*(n+1)
    for i in range(n):
        now = l[i]
        if (i+now[0]) <= n and d[now[0]] == 0:
            d[now[0]] = now[1]

    return
n = int(input())
l = []
for _ in range(n):
    l.append(list(map(int, input().split())))
print(toisa(n, l))
def toisa(n, l):
    d = [0]*(n+1)
    for i in range(n):
        now = l[i]
        if i + now[0] < n:
            d[i] = max(d[i-now[0]]+now[1], d[i])
    return d[n]

n = int(input())
l = []
for _ in range(n):
    l.append(list(map(int, input().split())))
print(toisa(n, l))
def toisa(n, l):
    d = [0]*(n+1)
    for i in range(n-1, -1, -1):
        nowt = l[i][0]
        nowp = l[i][1]
        if i + nowt <= n:
            d[i] = max(d[i+nowt]+nowp, d[i])
    return d[0]
    # 0 0 10 30 0 45

n = int(input())
l = []
for _ in range(n):
    l.append(list(map(int, input().split())))
print(toisa(n, l))
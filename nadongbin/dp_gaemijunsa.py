def gami(l, n):
    d = [0]*(n+1)
    visited = [False]*n
    # d[0], visited[0] = l[0], True

    for i in range(n):
        if i < 2:
            val = l[i]
        else:
            val = d[i-1]+l[i]
        if val > d[i]:
            d[i+1] = val
            if i == 0:
                visited[i] = True
            else:
                visited[i-1], visited[i] = False, True
        else:
            d[i+1] = d[i]
    return d[n]

n = int(input())
l = list(map(int, input().split()))
# print(gami(l, n))
d = [0]*n
d[0] = l[0]
d[1] = max(l[0],l[1])
for i in range(2, n):
    d[i] = max(d[i-1], d[i-2]+l[i])
print(d[n-1])
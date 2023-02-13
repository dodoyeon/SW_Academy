# 크림 파스타
def cream(n, l):
    d = [0]*n
    m = l[0]
    for i in range(1, n):
        val = (l[i]-m)
        if val > 0:
            d[i] = max(val, d[i-1])
        else:
            m = l[i]
            d[i] = d[i-1]
    return d

n = int(input())
l = list(map(int, input().split()))
print(*cream(n, l), sep=' ')
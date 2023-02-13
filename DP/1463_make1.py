# 1로 만들기 문제
def make1(n):
    d = [i for i in range(n, -1, -1)]
    # d = [0]*(n+1)
    for i in range(n, 0, -1):
        d[i-1] = min(d[i-1], d[i] + 1)
        if i%2 == 0:
            d[i//2] = min(d[i//2], d[i]+1)
        if i%3 == 0:
            d[i//3] = min(d[i//3], d[i]+1)
    return d[1]

def make2(n):
    d = [0]*(n+1)
    for i in range(2, n+1):
        d[i] = d[i-1]+1
        if i%2 == 0:
            d[i] = min(d[i//2]+1, d[i])
        if i%3 == 0:
            d[i] = min(d[i//3]+1, d[i])
    return d[n]

n = int(input())
print(make2(n))
print(make1(n))
# 18 = 6 2 1 7 = 6 2 1 25=24 8 4 2 1
# 14 = 7 6 2 1
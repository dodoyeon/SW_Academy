# 타일 장식물 = similar with fibonacci
def tile(n):
    if n == 1:
        return 4
    d = [0]*(n+1)
    d[1], d[2] = 1, 1
    for i in range(3, n+1):
        d[i] = d[i-1]+d[i-2]
    return 2*(2*d[n]+d[n-1])

n = int(input())
print(tile(n))
# 1로 만들기
def make1(n):
    if n == 1:
        return 0
    d = [0]*(n+1)
    for i in range(2, n+1):
        d[i] = d[i-1]+1
        if i%2 == 0:
            d[i] = min(d[i], d[i//2]+1)
        if i%3 == 0:
            d[i] = min(d[i], d[i//3]+1)
    return d[n]

n = int(input())
print(make1(n))
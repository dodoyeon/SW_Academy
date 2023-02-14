# 점화식
def t(n):
    d = [0]*(n+1)
    d[0] = 1
    for i in range(1, n+1):
        for j in range(i//2):
            d[i] += 2*(d[j]*d[i-j-1])
        if i%2 == 1:
            d[i] += d[i//2]**2
    return d[n]

n = int(input())
print(t(n))
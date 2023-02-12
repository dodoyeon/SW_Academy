# 피보나치 비스무리한 수열
def fibosim(n):
    if n < 3:
        return 1
    d = [0]*(n+1)
    d[1], d[2], d[3] = 1, 1, 1
    for i in range(3, n+1):
        d[i] = d[i-1] +d[i-3]
    return d[n]

n = int(input())
print(fibosim(n))